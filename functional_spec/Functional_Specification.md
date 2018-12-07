## Table of Contents:

**1.Introduction**
       
        1.1 Overview

        1.2 Business Contexts
	
        1.3 Glossary

**2.Description**

        2.1 Product/System Function

        2.2 User Characteristics and Objectives

        2.3 Operational Scenarios

        2.4 Constraints

**3.Functional Requirements**

        3.1 Edit User Preferences

        3.2 Request Transport Data
        
        3.3 Request Directions

        3.4 Favouriting Data
        
        3.5 Unfavouriting Data

        3.6 Giving Feedback

**4.System Architecture**

        4.1 System Architecture Diagram

        4.2 APIs

        4.3 Chatbot

        4.4 Messenger

**5. High-Level Design**

        5.1 High Level Design Schedule

        5.2 High Level Description

**6.  Preliminary Schedule**

        6.1 Overview of preliminary schedule

        6.2 Task List

        6.3 GANTT Chart

**7. Appendices**

        7.1 Resources and Research Data

## Section 1 - Introduction:

**1.1 Overview:**

The idea behind the project is an internet-based chat bot integrated into Messenger for Facebook. It will allow user to interact with it in a variety of ways and make requests for information about public transport. It will then interact with public transport APIs in order to gather the requested information and relay it back to the user.

This chat bot was developed in order to serve the commuting needs of the user. They can enter where they are at present or where they wish to travel from and their destination. He chatbot would then interact with the public transport APIs and return the best method of transport.

Another feature we are going to try to implement is that if the user needs directions on how to get the method of transport the chatbot can return the fastest way to get there for example directions from the spire to Tara Street train station. We hope to add this feature by using Google Maps direction API but this will be a secondary goals as we need to get our functionality up and running first so that we can get the data back to the user.

**1.2 Business Context:**

There are a few business contexts related to this project.

- **Forming a separate app:**

The system could be made into its own separate application which would replace the need for going online to look up the required information as it would all be contained within its own application. It could be developed as a replacement to the dublin bus app and instead be used as a hub for all public transport.

- **Ads:**

We could integrate travel specific ads into the bot for example it could recommend getting a leap card and where to get one in order the save user money on recurring journeys such as traveling to work or college.

- **Sell the product:**

The product could in theory be sold to the Transport Authority of Ireland and this would allow them to integrate more features into the system or take features from the system to be used in other project which they have.

**1.3 Glossary of terms:**

- **API:**

Acronym for Application Programming Interface

It's a set of routines protocols and tools used for building software applications. It specifies how certain software components should interact.

- **RTPI:**

Acronym for Real Time Passenger Information. Contains real-time, bus stops, route information for Dublin bus.

## Section 2 - General Description:

**2.1 Product/System Functions:**

This is a list of the main function we wish to include in our project, this is only a first round list and functions can be added or removed later. Each function will be described in detail in the 3rd section of this document.

- Entity Recognition
- Edit Preferences
- Request Directions
- Request Transport Data
- Favouriting Information
- Unfavouriting Information
- Give feedback

**2.2 User Characteristics and Objectives:**

Since the system we be a web-based chat bot based on WhatsApp or Messenger for Facebook, our system will be accessible to anyone who has an internet capable device and an account on these services. We hope to target anyone who commutes regularly be it to and from work, college or school, although it can be used by anyone when they need info about public transport information.

The User Interface will match the look of the app we decide to integrate the chatbot into for example the white and blue colour scheme of messenger. This would be done as users of such platforms would be most comfortable with this and we don't want to overload them with unnecessary features.

The moderation of the system will just be the already in place by either Facebook or WhatsApp meaning you need to be at least 16 to have a WhatsApp account. As we only plan to have the Chatbot return travel data we feel moderation won't be a huge issue

 **2.3 Operational Scenarios:**

There are three main scenarios of our system. Our scenarios involve querying the chatbot for information, bookmarking favourite information and giving feedback.

- **Querying the Chatbot:**

Querying the chatbot is the main functionality of our idea. The user inputs the what information they are looking for and the chatbot interprets the query, retrieves the information from the various APIs, processes the information and the presents it in a readable format for the user.

- **Bookmarking favourite information:**

We implemented bookmarking favourite information to improve usability. Once the chatbot has presented the user's desired information the user will have the option to bookmark the information for future reference. The user can access their bookmarked information by typing in a command

- **Giving Feedback**

Once information is presented from the chatbot or when the user is finished using the chatbot, they will have the option to rate the chatbot and its features. The results of the feedback will allow us to review the accuracy of the information provided and level of interaction the user has with the chatbot.

 **2.4 Constraints**

The constraints on this project are the deadline, reliability of APIs and the transport service and limitations of the range of our entity recognition. These are described in detail below.

- **Entity Recognition**

Entity Recognition involves taking in user input, analysing the input and tries to match it to one of our base cases. This makes matches based off analysing the relevant nouns and matches it to our base cases to query the APIs. We need to make sure we have a sufficient range of base cases in order to encounter these matches.

- **Reliability of transport services APIs**

The transport service APIs are under a lot of pressure due to an overwhelming amount of real time information user requests.This resulted in the server crashing.Currently VIX, used to meassure the expected volatility of a system, is being used.The service providers have stated that additional CPU services will be implemented into the servers to deal with this issue
- **Deadline**

As this app involves a chatbot with entity recognition, with time the ability of the program to correctly analyse user input would improve. Also with user's feedback, we could work on and improve on any negative feedback received.

**       **

## Section 3 – Functional Requirements

**3.1 Entity Recognition**

- **Description:**

Entity recognition involves processing text and classifying the different aspects of the text into pre-determined categories or base cases.This allows the chatbot to understand the user's input and request the desired information, then relay it back to the user.

- **Criticality:**

This is an essential function to our project.Without this there would be no interaction between the user,chatbot and the APIs.

- **Technical Issue**

We will have to make sure the aspects of the text are classified into the correct categories.
 
 - **Dependencies**

Entity recognition is completely reliant on the base cases which we provide.The more base case we provide the more accurately the data will be classified.

**3.2 Edit Preferences:**

- **Description:**

This will allow the user to edit their preferences, they can choose which age range they are in and  if they would like cheaper travel or don't mind paying a bit more. This would be used in for returning the prices of transport back to the user.

- **Criticality:**

This is not an essential function but would be very helpful when showing prices we hope to be able to implement this but it will not be a priority

- **Technical Issue:**

Getting the price data for the modes of transport and returning this to the user depends on a lot of variables.

- **Dependencies:**

This not depend on any other functions.

**3.3 Request Transport Data:**

- **Description:** 

This will be the main function of the project. The user will request info and the chatbot will query the APIs in order to find the required data . Once the data has been found it will then process the data and return it to  the user.

- **Criticality:** 

Since this will be the main function of the project this is vital and will be the main focus during the development and we strive to complete this before getting the chatbot working as we need to be able to gather the data for the chatbot to output

- **Technical Issue:**

The API will handle gathering the data then it will be up to us to process the data in a coherent method which we can the return to the user.

- **Dependencies:**

This will depend on entity recognition to find out what the user is asking for.

**3.4 Request Directions:**

- **Description:**

This is will allow the user to request directions from where they are now to where they can get the desired method of public transport. The chatbot will return a list of directions in a message in the chat interface.

- **Criticality:**

This is the second major function of the project since the user will request public transport data but may not know how to get to where they can get the bus/train  from so we feel it is necessary to let the user know how to get there.

- **Technical Issues:**

The gathering of the directions relies on being able to access the uses current location and OpenStreetMap API in order.

- **Dependencies:**

 None this will be implemented using OpenStreetMap APIs

**3.5 Favouriting information:**

- **Description:**

This will allow the user to mark a message containing route information or directions which they frequently use a s favourite to allow them to refer back to it quickly and easily at a later date.

- **Criticality:**

This is not an essential part of the project but it would add valuable functionality to the project and would also improve quality of life when using the chatbot

- **Technical Issue:**

We will have to make sure the information is correctly  appended to the saved information list.

- **Dependencies:**

Depends on Requesting Transport Data

**3.6 Unfavouriting Information:**

- **Description:**

If the users feels they no longer need the information which they previously had in their favourites they can then remove it from this list.

- **Criticality:**

This also is not an essential part of the project but would also add to the quality of  life while  using our chatbot

- **Technical Issues:**

We have to make sure the right information is removed from the list of  favourites

- **Dependencies:**

This will also depend on requesting the transport data but will depend on the information being favourited

**3.7 Giving Feedback:**

- **Description:**

This will allow the user to give feedback on the data they received and how accurate it was. After each instance of getting transport data that chatbot will ask you to rate the accuracy of the data you received.

- **Criticality:**

This will be a main function as we will use this feedback in order to improve the entity recognition and be able to give more accurate information in the future

- **Technical Issue:**

We have to know when the interaction is over to then request feedback

- **Dependencies:**

This depends on returning data to the user

## Section 4 – System Architecture:

**4.1 System Architecture Diagram**

##


**Fig 4.1** The above diagram illustrates the architecture of our program. As seen in the above diagram there are four main aspects of the system architecture. The user (which is the front end, what users see and input),messenger(interface for the user and chatbot), Chatbot (what the user and APIs interact with ) and the APIs (the chatbot will interact with these to retrieve desired information) all make-up the system architecture.

### **4.2 APIs**

The APIs are the back end of our chatbot, these will gather the data that is required by the user. It will be made up of  multiple public transport APIs which depending on what the user enters will be called in order to gather the requested data. The APIs will interact with the code making up the chatbot in order to pass information to and from.

### **4.3 Chatbot**

This will be what contains our base cases for entity recognition in the users input, once the input is parsed and the entity is found it will then pass this information on the APIs in order to gather the data and then pass back the data that is found to messenger to be given to the users.

### **4.4 Messenger:**

This will be how the user interact with the chatbot, it will act as any normal chat on Facebook since the user will most likely be familiar with how the User Interface works and won't need to learn how to use all the features.
## Section 5 - High-Level Design:

**5.1 High-Level Design Diagram:**
















**5.2 High-Level Design Description:**

**Fig 5.1** is explained below

- **Step 1: Sign Up for Bot use**

The user will go and signup to use the bot and add it to their list of chats.

- **Step 2: Enter Your Preferences**

The user then enters their preferences for example they would enter their name, their ages range and if they prefer cheaper transport. This allows the chatbot to pick the most relevant data for each user.

- **Step 3: User Requests Data**

The user can then request data from the chat bot. for example the user can ask how they can get from skerries to O'Connell Street.

- **Step 4: Chat Bot Gathers Data**

The chat bot will then interact with the public transport API's to try to gather the data that user has request this data could range from timetables of trains or buses to directions current location

- **Step 5: Chat Bot Returns Data**

The chatbot will then return the data to the user in a clear and concise manner to the user.  It will follow the User Interface of the app we integrate the chat bot into. It will return the data as a message much like a text conversation.

- **Step 6: User End Chats**

Once the user is finished using the chat bot, the user can close the chat like they would any other chat, they can then re-open the chat if they wish to use it again

## Section 6 – Preliminary Schedule

**6.1 Overview of Preliminary Schedule:**

The task list contains the list of tasks that we need to accomplish in order to get the project working. The list contains the name of the task, the due date, the day the task is started, the day the task should be completed by and the name of the team member working on the specific.

### **6.2 Task List:**


### **6.2 GANTT Chart**

## Section 7 – Appendices

### **7.1 - Resources and Research Tools:**

Website for public transport:

[https://data.smartdublin.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail](https://data.smartdublin.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail)

Data for public transport:

[https://www.transportforireland.ie/transitData/PT\_Data.html](https://www.transportforireland.ie/transitData/PT_Data.html)

Rail API:

[http://api.irishrail.ie/realtime/index.htm?realtime\_irishrail](http://api.irishrail.ie/realtime/index.htm?realtime_irishrail)

Bus API:

[https://data.smartdublin.ie/dataset/c9df9a0b-d17a-40ff-a5d4-01da0cf08617/resource/4b9f2c4f-6bf5-4958-a43a-f12dab04cf61/download/rtpirestapispecification.pdf](https://data.smartdublin.ie/dataset/c9df9a0b-d17a-40ff-a5d4-01da0cf08617/resource/4b9f2c4f-6bf5-4958-a43a-f12dab04cf61/download/rtpirestapispecification.pdf)

OpenStreetMap:

[http://overpass.openstreetmap.ie/](http://overpass.openstreetmap.ie/)

[http://overpass-turbo.eu/](http://overpass-turbo.eu/)


