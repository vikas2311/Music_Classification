import eyed3
import os
import shutil

class example:

     @staticmethod
     def create_directory(src_file1,artist_name,artist_name_array):
        #Creating a directory by the artist name
            dirName = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/"+artist_name
            source_file_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/" + src_file1
            print("source_file_path => ",source_file_path)
            destination_folder = dirName
            index_artist=artist_name_array.index(artist_name)
            print("index_artist",index_artist)
            print(index_artist==len(artist_name_array) - 1)

            count_array = len(artist_name_array) - 1
            if not index_artist == count_array :
                #print(os.getcwd())
                print("########",artist_name)
                print("dirName => ",dirName)
                try:
                    # Create file's destination directory 
                    if not os.path.exists(dirName):
                        os.makedirs(dirName)
                        print("Directory ->" , dirName ,  "<- Created :)")

                        #Moving the File to created directory.
                        print("source_file_path => ",source_file_path)
                        print("destination_folder => ",destination_folder)
                        
                        if src_file1.endswith(".mp3"):
                            shutil.copy(source_file_path,destination_folder)
                            print("File copied to Destination path. :)")

                        else:
                            print("File Moving Failed. :(")

                    else:    
                        print("Directory " , dirName ,  " already exists :(" ) 
                        shutil.move(source_file_path,dirName)
                        print("File Moved to Destination path. :)")

                except OSError:
                    print("Creation of the directory %s failed :(" % dirName)
            else:
                print("Else---index_artist",index_artist)
                print(index_artist==len(artist_name_array) - 1)
                if src_file1.endswith(".mp3"):
                    os.makedirs(dirName)
                    print("Directory ->" , dirName ,  "<- Created :)")
                    print("source_file_path => ",source_file_path)
                    print("destination_folder => ",destination_folder)
                    shutil.copy(source_file_path,destination_folder)
                    print("File copied to Destination path. :)")
                    os.remove(source_file_path)
                    print("File Removed after copying for last artist.")



try:
        
        mp3_file_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/Barsaat.mp3"
        music_Files_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/"

        source_files=os.listdir(music_Files_path)
        print(source_files)
        for src_file in source_files:
            print(src_file)
            if src_file.endswith(".mp3"):
                print(src_file.endswith(".mp3"))
                
                
                audiofile = eyed3.load(music_Files_path+src_file)
            
                '''
                print("##")
                print(audiofile)
                print("##")
                '''

                artist_name =audiofile.tag.artist
                print("artist_name => ",artist_name)
                artist_Name_Array=artist_name.split(",")

                print(" artist_Name_Array =>",artist_Name_Array)

                artist_Name_Array=[x.strip() for x in artist_Name_Array if x.strip()]
                print(artist_Name_Array)


                album_name=audiofile.tag.title

                for item in artist_Name_Array:
                    print(item.strip())
                    item=item.strip()
                    
                    print("****",item)
                    print("****",not item)
                    example.create_directory(src_file,item,artist_Name_Array)

            else:
                print("Not an mp3 :(")

except IOError:
    print("File not found")
    