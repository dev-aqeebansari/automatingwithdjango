from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CompressImageForm
from PIL import Image
import io
# Create your views here.

def compress(request):
    user = request.user
    if request.method == 'POST':
        form = CompressImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_image = form.cleaned_data['original_image']
            quality = form.cleaned_data['quality']

            compressed_image = form.save(commit=False) #saving form temporarily
            compressed_image.user = user

            #perform compression
            image = Image.open(original_image)
            output_format = image.format
            buffer = io.BytesIO()
            # print('cursor position before image compression=>', buffer.tell()) 
            image.save(buffer, format=output_format, quality=quality)
            buffer.seek(0)
            #save the compressed image inside the model
            compressed_image.compressed_image.save(
                f'compressed_{original_image}', buffer
            )

            #Automatically download the compressed file
            response = HttpResponse(buffer.getvalue(), content_type =f'image/{output_format.lower()}')
            response['Content-Disposition'] = f'attachment; file_name=compressed_{original_image}'
            return response
            # return redirect('compress')
    else:
        form = CompressImageForm()
        context = {
        'form' : form,
    }
    return render(request, 'image_compression/compress.html', context)