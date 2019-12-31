import eyed3
import os
import shutil

try:
    
    #mp3_file_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/Barsaat.mp3"
    music_Files_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/"

    source_files=os.listdir(music_Files_path)
    for src_file in source_files:
        print("****",src_file,"*****")
        
        if src_file.endswith(".mp3"):
           # print(src_file.endswith(".mp3"))
                       
            audiofile = eyed3.load(music_Files_path+src_file)
          
            '''
            print("##")
            print(audiofile)
            print("##")
            '''

            artist_name =audiofile.tag.artist
            print("\t artist_name => ",artist_name)
            album_name=audiofile.tag.title

         #Creating a directory by the artist name
            #print(os.getcwd())
            dirName = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/"+artist_name
            print("\t dirName => ",dirName)
            try:
                # Create file's destination directory 
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
                    print("\t Directory Created ->" , dirName ,  "<- Created :)")

                    #Moving the File to created directory.
                    source_file_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/" + src_file
                    destination_folder = dirName

                    print("\t source_file_path => ",source_file_path)
                    print("\t destination_folder => ",destination_folder)
                    
                    if src_file.endswith(".mp3"):
                        shutil.move(source_file_path,destination_folder)
                        print("File Moved to Destination path. :)"," \n")

                    else:
                        print("File Moving Failed. :(")

                else:    
                    print("\t Directory " , dirName ,  " already exists :( \n" ) 
            except OSError:
                print("Creation of the directory %s failed :( \n" % dirName)
        else:
            print("Not an mp3 :( \n")
except IOError:
    print("File not found \n")
 