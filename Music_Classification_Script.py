import eyed3
import os
import shutil

class Music_Classification_Script:

    @staticmethod
    def makeDir_Copy(source_file_path,destination_folder):
        print("\t Directory made.")
        os.makedirs(destination_folder)
        shutil.copy(source_file_path,destination_folder)
        print("\t File Copied in FOlder \n")

    @staticmethod
    def makeDir_move(source_file_path,destination_folder):
        print("\t Directory made.")
        os.makedirs(destination_folder)
        shutil.move(source_file_path,destination_folder)
        print("\t File moved in FOlder \n")

        

    @staticmethod
    def create_directory(music_file,artist_Name_List):     
      '''
      artist_Name_List : ['A. R. Rahman', 'Jonita Gandhi', 'Nakash Aziz']
      music_file : xyz.mp3
      ''' 
      #Iterate over the artist in the Artist List:   
      for artist_name in artist_Name_List:
            '''
            source_file_path : Folder *from* which music file is to be moved.
            destination_folder : Folder *to* which music file is to be moved.
            '''
            destination_folder = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/" + artist_name
            source_file_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/" + music_file
            #print("source_file_path => ",source_file_path)
            
            #Needed to check if artist is the last element in the artists list:
            index_artist=artist_Name_List.index(artist_name)
            #print("index_artist",index_artist)
            #print("artist the last element in the list: ",index_artist==len(artist_Name_List) - 1)
            #print(artist_name)

            #artist not the last element in the artists list:
            if(not index_artist==len(artist_Name_List)-1):
                print(">>>>>> ",artist_name)               
                try:               
                    #path for this artist does not exists:
                    if not os.path.exists(destination_folder):
                        #Make a directory and copy the file:
                        print("\t Path does not exists. ")
                        Music_Classification_Script.makeDir_Copy(source_file_path,destination_folder)      

                    #Path for this artist exists:
                    else:
                        print("\t Path exists.")
                        shutil.copy(source_file_path,destination_folder)
                        print("\t File copied to Destination path. :) \n")
                       
                except OSError:
                    print("creation of directory failed. \n")

            #artist is the last element in the artists list:
            else:
            #Move the last to its directory:
                try:
                    print(">>>>>> ",artist_name," - *(last artist in artist name list.)")      
                    #If path for this artist does not exists:
                    if not os.path.exists(destination_folder):
                        #Make a directory and Move the file:
                        print("\t Path does not exists. ")
                        Music_Classification_Script.makeDir_move(source_file_path,destination_folder)

                    #Path for this artist exists:
                    else:
                        print("\t Path exists. ")
                        shutil.copy(source_file_path,destination_folder)
                        print("\t File copied to Destination path. :)")
                        #Remove the given file 
                        os.remove(source_file_path)
                        print("\t File Removed after copying for last artist. \n")
                except OSError:
                    print("creation of directory failed. \n")


try:        
        #Music Folder For Classification.
        music_Files_path = "c:/Users/Vikas.Singh3/Desktop/Learning Programming/Music_Files/"

        #Extract all files from the given folder:
        source_files=os.listdir(music_Files_path)
        #print(source_files)

        #Iterate over the Files in the source Folder:
        for src_file in source_files:
            try:
                print("****",src_file,"*****")
                if src_file.endswith(".mp3"):
                    music_file = src_file#Source file is a music file.
                
                    #Load the Mp3 from the given path into given variable.
                    audiofile = eyed3.load(music_Files_path + music_file)            
                    '''
                    print("##")
                    print(audiofile)
                    print("##")
                    '''
                    #Extract artist name from Mp3 into variable.
                    artist_name =audiofile.tag.artist
                    print("artist_name => ",artist_name)
                    #song_title = audiofile.tag.title
                    #music_file = song_title[:song_title.rindex(" ")] + ".mp3"          
                    artist_Name_List=artist_name.split(",")
                    print("artist_Name_List =>",artist_Name_List)

                    # To Strip spaces from the list as well as individual artists in the list:
                    artist_Name_List=[x.strip() for x in artist_Name_List if x.strip()]
                    print(artist_Name_List)
                    album_name=audiofile.tag.title

                    # Method to create directory to create folders for artists in the artist list:
                    Music_Classification_Script.create_directory(music_file,artist_Name_List)
            
                #File in the Source Folder is not an Mp3
                else:
                    print("Not an mp3 :( \n")
            #File Not Found.
            except OSError:
                print("File not found :( \n")
except OSError:
    print("Directory doesn't Exist. \n")
    