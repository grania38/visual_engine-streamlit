import streamlit as st
import requests
import pymongo

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img

@st.cache
def calcDistance(pic1,pic2):
    result=float(0)  
    for i in range(0,len(pic1)):
         result+=(float(pic1[i])-float(pic2[i]))**2
    return result

def main():

    image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
    data_load_state = st.text('Loading image...')

    if image_file is not None:

	    # To See Details
        #st.write(type(image_file))
        #st.write(dir(image_file))
        file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
        st.write(file_details)
        img = load_image(image_file)
        data_load_state.text("Done! (using st.cache)")
        st.image(img,width=250,height=250)
"""
    # Initialize connection.
    [mongo]
    host = "localhost"
    port = 27017
    #username = "gharbir808"
    #password = "Bonjour123456!"

    client = pymongo.MongoClient(**st.secrets["mongo"])

    # Pull data from the collection.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def get_data():
        db = client.imageDB
        items = db.images.find()
        items = list(items)  # make hashable for st.cache
        return items

    items = get_data()

    index = file.filename.split('.')[0]

        index = int (index)

        cluster=collection.find({"index":index})[0]["cluster"]

        cluster_picture_edge=[]

        for col in collection.find({"cluster":cluster}):

            cluster_picture_edge.append(col)
     
   similar_picture=[{"result":0,"index":cluster_picture_edge[0]["index"]}]
    
    for item in items:
        print(item)


    
   

"""

if __name__=='__main__':
    main()