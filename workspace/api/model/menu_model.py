import numpy as np
from PIL import Image
import tensorflow as tf

class MenuModel():
    """
    入力(冷蔵庫内の)画像から献立クラスを返すクラス
    """
    def __init__(self, model_path):
        self.menu_model =  tf.keras.models.load_model(model_path)
        
    def _imageloader_from_path(self, image_path):
        return np.array(Image.open(image_path).resize((480,360))).transpose(1,0,2)
    
    def _imageloader_from_list(self, image_list):
        return np.array(image_list.resize((480,360))).transpose(1,0,2)
    
    def _imageloader(self, image_list, image_path):
        """
        image_list or image_path から 入力画像を読み込むメソッド
        
        Parameters
        ----------
        image_list : list
            image画像のリスト(横，縦，3(RGB))
        image_path : str
            image画像が保存されてる場所のURL
            
        Returns
        -------
        return : array
            (480,360,3)の画像を返す 
        """
        if (image_list!=None) and (image_path!=None) :
            return self._imageloader_from_list(image_list)
        elif (image_list==None) and (image_path!=None) :
            return self._imageloader_from_path(image_path)
        elif (image_list!=None) and (image_path==None) :
            return self._imageloader_from_list(image_list)
        else:
            print("Please input either image_list or image_path.")
            return None
        
    def pred_class(self, image_list=None, image_path=None):
        """
        画像の配列 or 画像のURL から 献立クラスを返すメソッド．
        image_list か image_path に値を代入すると，
        予想される献立クラス(0~3)をreturnする．
        
        Parameters
        ----------
        image_list : list
            image画像のリスト(横，縦，3(RGB))
        image_path : str
            image画像が保存されてる場所のURL
            
        Returns
        -------
        predict : int
            予想される献立クラス(0~3)
        """
        image = self._imageloader(image_list, image_path)
        predict = np.argmax(self.menu_model.predict(image.reshape(1,480,360,3)))
        return predict