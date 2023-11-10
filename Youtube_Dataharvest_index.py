# Import components
import pandas as pd
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

from PIL import Image
from io import BytesIO
import time
import requests

# File Import
from Database_Function import*

# Page Title
st.set_page_config(page_title= "Youtube Dataharvest and Warehousing",page_icon= 'bar_chart', layout= "wide")

# Main Page
st.markdown('### 📊 **:green[YouTube Data Harvesting and Warehousing using SQL MongoDB and Streamlit]**')

st.markdown("""
<style>
	.stTabs [data-baseweb="tab"] {
		height: 30px;
        width: 700px;
        white-space: pre-wrap;
		background-color:#FF4B4B;
        color: #FFFFFF;
		border-radius: 4px 4px 0px 0px;
		gap: 13px;
		padding-top: 20px;
		padding-bottom: 20px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
        color:#FF4B4B;
	}

</style>""", unsafe_allow_html=True)

# Menu 
tab_titles = [' 💬  Home', '🧾 Data Migrate to Mongodb', '📝 Data Migrate Mongodb to SQL', '📈 Data Analaysis']
tab1, tab2, tab3, tab4 = st.tabs(tab_titles)
 
    
# Add content to each tab

#Home Tab 
with tab1:    
    st.markdown(":blue[Project Title:]  YouTube Data Harvesting and Warehousing using SQL, MongoDB and Streamlit")
    st.markdown(":blue[Skills:]  Python scripting, Data Collection, MongoDB, Streamlit, API integration, Data Management using MongoDB and SQL")  
    st.markdown(":blue[Domain:]  Social Media (Youtube Data Analysis)") 
    st.markdown("**Introduction**")
    st.markdown("The goal of the YouTube Data Harvesting and Warehousing project is to render data from various YouTube channels, open to users for analysis. Using SQL, MongoDB, and Streamlit, the project develops a user-friendly application that lets users store, retrieve, and query data related to YouTube channels and videos..")
    st.markdown(" **Project Overview**")
    st.markdown(" This project consists of the following components:")
    st.markdown(" **Streamlit:**  A user-friendly user interface (UI) created with the Streamlit library. Streamlit is a great choice for building data visualization and analysis tools quickly and easily.")  
    st.markdown(" **YouTube API Integration:**  Integration with the YouTube API to retrieve video and channel information by entering the channel ID.") 
    st.markdown(" **MongoDB:** The data that was retrieved from Youtube is stored in a MongoDB database, it is used for storing unstructured data. ") 
    st.markdown(" **SQL:** Migrate data from the MongoDB data lake to a SQL database.") 
    st.markdown(" **Data Analysis:** Using Streamlit, provide the user with a few query options. From that menu, choose a question to analyse the data and display the results in a Dataframe Table and Bar Chart.") 

# Data Migrate into MongoDB
with tab2:
    # Header
    st.header('Data Migrate into MongoDB')
    left,center=st.columns([3.5,6.5])
    with left:
        # Get Channel Id
        channel_id=st.text_input('Enter channel ID:')
        if st.button('SEARCH'):
            with st.spinner('Fetching Channel Details'):
          #Page Center Column for Displaying Channel Details
                with center: 
                    channel_data,channel_image = get_channel_data(youtube, channel_id)
                    col1, col2 = st.columns([2,3])
                # Channel Thumbnail Image
                    with col1:
                        if channel_data:
                            image = channel_image['image']
                            response = requests.get(image)
                            if response.status_code == 200:
                                image = Image.open(BytesIO(response.content))
                                new_image = image.resize((200, 200))
                                value = streamlit_image_coordinates(new_image)
                            else:
                                print('Failed to load an image.')
                        else:
                            print('Failed to get channel image')
                        
                    #Store Channel Data 
                    channel_name=channel_data["channel_name"]
                    channel_id=channel_data["channel_id"]
                    video_count=channel_data["video_count"]
                    subscribers_count=channel_data["subscribers_count"]
                    channel_description=channel_data["channel_description"][:100]
                    Channel_Type=channel_data["Channel_Type"]
                    playlist_id=channel_data["playlist_id"]
                    
                    #Display Channel Details
                    col2.write(f"**:blue[{channel_name}] - :blue[{channel_id}]**") 
                    col2.write(f"{subscribers_count} subscribers .{video_count} videos ")
                    col2.write(f"{channel_description} [..]") 
                    col2.write(f"Genre: {Channel_Type}") 
                    col2.write(f"Playlist Id: {playlist_id}") 
          
    if st.button('UPLOAD TO MONGODB DATABASE'):
        with st.spinner('uploading channel information ...'):
            with left:
                
                  #Fetching Data to upload in Mongodb                        
                    channel_data, channel_image = get_channel_data(youtube, channel_id)
                    channel_name = channel_data['channel_name']
                    playlist_id = channel_data['playlist_id']
                    video_id = get_video_ids(youtube, playlist_id)
                    video_data = get_video_data(youtube, video_id)
                    comment_data = get_comment_data(youtube, video_id)
                    channel=channel_video_comment(channel_id)
                    
                  #checking whether data exist or not and Insert into MongoDB
                    try:
                            check_existing_document = collection.find_one({"channel_info.channel_id": channel_id})
                            if check_existing_document is None:
                                collection.insert_one(channel)
                                st.success('Successfully uploaded ',icon='✔️')
                            else:
                                st.error(f" This Channel data already uploaded",icon='❌')
                    except Exception as e:
                            print(f"Error occurred while uploading channel information: {str(e)}")

# Data Migrate MongoDB to SQL
with tab3:
    mongo,sql=st.columns([2,2])
    
# fetching data from mongoDB
    with mongo:
        st.markdown("## MONGODB DATABASE")
        with st.spinner('Fetching the Data...'):
                channel_list=channel_list()
                option=st.selectbox('Channel List in Mongodb',['Please select channel name']+channel_list)

    for result in collection.find({"channel_info.channel_name": option}):
                channel_info = result['channel_info']
                video_info = result['video_info']
                st.write("### Channel Data ")
                st.write(channel_info,video_info)


    # Migrating data to Mysql database
    with sql:
            st.markdown('## MIGRATE DATA FROM MONGODB TO SQL ')
            if st.button('MIGRATE TO SQL'):                 
                    channel_name_to_find = option
                    channel_df, playlist_df,video_df, comment_df = Mongo_to_SQL(channel_name_to_find)
                    with st.spinner('uploading channel data to sql ...'):
                    
                    # Migrate data to SQL database
                        channel_df.to_sql('channel_data', con=engine, if_exists='append', index=False)
                        playlist_df.to_sql('playlist_data',con=engine, if_exists='append', index=False)
                        video_df.to_sql('video_data',con=engine, if_exists='append', index=False)
                        comment_df.to_sql('comment_data', con=engine, if_exists='append', index=False)
                        st.success(f"{channel_name_to_find} channel migrated successfully", icon='✅')
#SQL Given Query                    
with tab4:
    st.header('CHANNEL DATA ANALYSIS')
    select_question = st.selectbox("SQL Query", ('Select Query Here',
                     '1. What are the names of all the videos and their corresponding channels?',
                     '2. Which channels have the most number of videos, and how many videos do they have?',
                     '3. What are the top 10 most viewed videos and their respective channels?',
                     '4. How many comments were made on each video, and what are their corresponding video names?',
                     '5. Which videos have the highest number of likes and what are their corresponding channel names?',
                     '6. What is the total number of likes for each video and what are their corresponding video names?',
                     '7. What is the total number of views for each channel, and what are their corresponding channel names?',
                     '8. What are the names of all the channels that have published videos in the year 2022?',
                     '9. What is the average duration of all videos in each channel, and what are their corresponding channel names?',
                     '10. Which videos have the highest number of comments, and what are their corresponding channel names?'))

    if select_question== '1. What are the names of all the videos and their corresponding channels?':
         st.table(question_1())
    elif select_question=='2. Which channels have the most number of videos, and how many videos do they have?':
            st.table(question_2())
    elif select_question=='3. What are the top 10 most viewed videos and their respective channels?':
            st.table(question_3())
    elif select_question=='4. How many comments were made on each video, and what are their corresponding video names?':
            st.table(question_4())
    elif select_question=='5. Which videos have the highest number of likes and what are their corresponding channel names?':
            st.table(question_5())
    elif select_question=='6. What is the total number of likes for each video and what are their corresponding video names?':
            st.table(question_6())
    elif select_question=='7. What is the total number of views for each channel, and what are their corresponding channel names?':
            st.table(question_7())
    elif select_question=='8. What are the names of all the channels that have published videos in the year 2022?':
            st.table(question_8())
    elif select_question=='9. What is the average duration of all videos in each channel, and what are their corresponding channel names?':
            st.table(question_9())
    elif select_question== '10. Which videos have the highest number of comments, and what are their corresponding channel names?':
            st.table(question_10())


    

