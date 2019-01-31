# Amazon Advertising Automation Test Scenario & NLP Analysis
This project is divided into 2 parts:
- To build an automation scenario using Selenium Python
- To analyze Search keywords for identifying relevant patterns

#### Use Case:
For Sellers looking to advertise on the Amazon advertising platform using the "Sponsored Ads" option on the Amazon.com website. <br>
The seller's ads would be displayed for specific users depending on the "keywords" of the current search that the user is running. <br>
As such, it is important to identify relevant keywords/phrases that the seller could include in the display text/description of their ad, so that their products get maximum visibility & they get maximum clicks/buys/ROI.



### Part 1: (Testing/Automation for Product Search)
Filename: "ads_test.py" <br>
Objective: For the Sellers of Sony Camera, validate if for a search for the word "camera" displays results for Sony Camera or not on the first 5 Search Results pages. <br>
Test Scenario: Run an automated search on Amazon.com for the word "camera", & validate the 1st 5 pages for the keyword "Sony" <br>
Test Setup: Using Python's unittest framework & Selenium interface, driver for Mozilla Firefix Browser <br>
##### Test Steps: 
Test Case 1:
- Open "amazon.com" through the script
- Locate the search box
- Run a search with the keyword "camera"
- Send RETURN
- Verify that Search Results are not empty <br>

Test Results: Successfully Validated Search Results for "camera" are not empty


Test Case 2:
- Iterate through the first 5 pages of search results
- Find the Heading text of each displayed product
- Look for Sony in the text
- If found print validation success <br>

Test Results: Successfully validated "Sony" products displayed 6 times in Search Results for "camera" in the first 5 pages.

### Part 2: (Product Text Analysis using NLP techniques)
Filename: "ads-NLP.md" <br>
Objective: Identify relevant keywords for products that are displayed under the search keyword "camera" <br>
Scenario: Perform NLP text analysis on the list of product names from the 1st 5 pages for the search keyword "camera", and identify the most relevant keywords in Product descriptions. <br>
Setup: NLP ANalysis using R, Data retreival from Selenium Automation script <br>
##### Steps:
- Create a list of product names from TC2
- Store it as a csv
- Read the CSV in R
- Apply NLP techniques to perform text analysis
  - Identify the list of top/most frequently found common words in Product Descriptions
  - Perform Bigram analysis to identofy the top/most relevant phrases in Product Descriptions <br>

Results: 
- For search with the keyword "camera", the top products have the following most relevant keywords: camera, digital, hd, 1080p, zoom, lens
- Phrases such as "Digital camera", "Night vision", "Optical Zoom" are the most commonly used for camera related products

