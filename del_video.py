import os 
import re 
import openpyxl


check_path='./less10' #视频路径
excel_file='./chongfu.xlsx' #excel文件

class Util:

    def read_excel(self):
        wb=openpyxl.load_workbook(excel_file)
        sheet=wb.active
        self.vids=[]
        for row in sheet.iter_rows(min_row=2):
            self.vids.append(row[0].value)
        

    def get_files(self,dir):
        """
        获取所有的MP4文件
        """
        all_files=[]
        for root,dirs,files in os.walk(dir):
            for file in files:
                if file.endswith('.mp4'):
                    all_files.append(os.path.join(root,file).replace('\\','/'))
        return all_files

    def del_video(self,video_path):
        """
        删除视频及m4a、vtt文件
        """
        id=re.findall('[a-zA-Z0-9_-]{11}',video_path)[0]
        dir_path=os.path.dirname(video_path)
        files=os.listdir(dir_path)
        vtt_file,m4a_file=None,None
        for file in files:
            if id in file:
                if 'vtt' in file:
                    vtt_file=os.path.join(dir_path,file)
                elif 'm4a' in file:
                    m4a_file=os.path.join(dir_path,file)
        if vtt_file:
            os.remove(vtt_file)
        if m4a_file:
            os.remove(m4a_file)
        os.remove(video_path)
        print(f'删除视频：{video_path}及其相关文件')
    
    def main(self):
        #读取excel文件
        self.read_excel()
        # print(self.vids)
        #读取mp4文件
        videos=self.get_files(check_path)
        for video in videos:
            #判断vid是否在excel列表中
            id=re.findall('[a-zA-Z0-9_-]{11}',video)[0]
            if id in self.vids:
                #删除视频及m4a、vtt文件
                self.del_video(video)

if __name__ == "__main__":
    util=Util()
    util.main()
            