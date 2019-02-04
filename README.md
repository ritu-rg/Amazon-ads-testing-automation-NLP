# Amazon Advertising Automation Test Scenario & NLP Analysis
This project is divided into 2 parts:
- To build an automation scenario using Selenium Python
- To analyze Search keywords for identifying relevant patterns

#### Use Case:
For the Sellers running ads on the Amazon.com website using the "Sponsored Ads" option, their ads would be displayed for specific users depending on the "keywords" of the current search that the user is running. <br>
While creating their campaign on Amazon Advertising using Seller Central, they need to include these keywords/phrases in the list of keywords that their product should be displayed for. <br>
As such, it is important to identify relevant keywords/phrases that the seller could include in the the list of relevant keywords for their ads, so that their products get maximum visibility & they get maximum clicks/buys/ROI.



### Part 1: (Automated Test Scenario for Product Search on Amazon.com using Selenium Python)
Filename: "ads_test.py" <br>
Objective: For the Sellers of Sony Camera, validate if for a search for the word "camera" displays results for Sony Camera or not on the first 5 Search Results pages. <br>
Test Scenario: Run an automated search on Amazon.com for the word "camera", & validate the first 5 pages for the keyword "Sony" <br>
Test Setup: Using Python's unittest framework & Selenium interface, driver for Mozilla Firefox Browser <br>
##### Test Steps: 
Test Case 1:
- Open "amazon.com" through the script
- Locate the search box
- Run a search with the keyword "camera"
- Verify that Search Results are not empty <br>

Test Results: Successfully Validated Search Results for "camera" are not empty


Test Case 2:
- Iterate through the first 5 pages of search results
- Find the Heading text of each displayed product
- Look for Sony in the text
- If found print validation success <br>

Test Results: Successfully validated "Sony" products displayed 6 times in Search Results for "camera" in the first 5 pages.

### Part 2: (Product Text Analysis using Machine Learning - NLP techniques in R)
Filename: "ads-NLP.md" <br>
Objective: Identify relevant keywords for products that are displayed under the search keyword "camera" <br>
Scenario: Perform NLP text analysis on the list of product names from the first 5 pages for the search keyword "camera", and identify the most relevant keywords in Product descriptions. <br>
Setup: NLP Analysis using R, Data retreival from Selenium Automation script <br>
##### Steps:
- Create a list of product names obtained from Test Case 2 output
- Store it as a csv & read it in R
- Apply NLP techniques to perform text analysis
  - Identify the list of top/most frequently found common words in Product Descriptions
  - Perform Bigram analysis to identify the top/most relevant phrases in Product Descriptions <br>

Results: 
- For search with the keyword "camera", the top products have the following most relevant keywords: camera, digital, hd, 1080p, zoom, lens
- Phrases such as "Digital camera", "Night vision", "Optical Zoom" are the most commonly used for camera related products

 

