from PIL import Image, ImageOps

class DataAugmentation(object):
    def __init__(self, save_path):
        self.save_path = save_path
        
    def all_run(self, ref_path, filename, extension):
        im = Image.open(ref_path + filename + extension)
        im = self._base(im, filename, extension)
        im_flip = self._flip(im, filename, extension)
        im = self._combine(im, im_flip)
        im_mirror = self._mirror(im, filename, extension)
        im = self._combine(im, im_mirror)
        im_rotate = self._rotate(im, filename, extension)
        im = self._combine(im, im_rotate)
        im_contrast = self._contrast(im, filename, extension)
        im = self._combine(im, im_contrast)
    
    def _combine(self, old, new):
        return old + new
    
    def _save(self, im, filename, process, number, extension):
        save_name = self.save_path + filename + process + str(number) + extension
        im.save(save_name, quality=75)
        
    def _base(self, im, filename, extension):
        self._save(im, filename, "_org", 0, extension)
        return [im]
    
    def _flip(self, ims, filename, extension):
        im_list = []
        for i, im in enumerate(ims): 
            im_flip = ImageOps.flip(im)
            im_list.append(im_flip)
            self._save(im_flip, filename, "_flip", i, extension)
        return im_list
    
    def _mirror(self, ims, filename, extension):
        im_list = []
        for i, im in enumerate(ims): 
            im_mirror = ImageOps.mirror(im)
            im_list.append(im_mirror)
            self._save(im_mirror, filename, "_mirror", i, extension)
        return im_list
    
    def _rotate(self, ims, filename, extension, angles=[72,144,216,288]):
        im_list = []
        for i, im in enumerate(ims): 
            for j, angle in enumerate(angles):
                im_rotate = im.rotate(angle, resample=Image.BICUBIC)
                im_list.append(im_rotate)
                self._save(im_rotate, filename, "_rotate", 10*i+j, extension)
        return im_list
            
    def _contrast(self, ims, filename, extension, rates=[5,10]):
        im_list = []
        for i, im in enumerate(ims): 
            for j, rate in enumerate(rates):
                im_contrast = ImageOps.autocontrast(im, rate)
                im_list.append(im_contrast)
                self._save(im_contrast, filename, "_contrast", 10*i+j, extension)
        return im_list