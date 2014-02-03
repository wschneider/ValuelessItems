     __                      _                                               |
  /\ \ \___  ___  _ __   ___| |_ ___                                         |
 /  \/ / _ \/ _ \| '_ \ / _ \ __/ __|                                        |
/ /\  /  __/ (_) | |_) |  __/ |_\__ \                                        |
\_\ \/ \___|\___/| .__/ \___|\__|___/                                        |
                 |_|                                                         |
             _            _                  _____ _                         |
 /\   /\__ _| |_   _  ___| | ___  ___ ___    \_   \ |_ ___ _ __ ___  ___     |
 \ \ / / _` | | | | |/ _ \ |/ _ \/ __/ __|    / /\/ __/ _ \ '_ ` _ \/ __|    |
  \ V / (_| | | |_| |  __/ |  __/\__ \__ \ /\/ /_ | ||  __/ | | | | \__ \    |
   \_/ \__,_|_|\__,_|\___|_|\___||___/___/ \____/  \__\___|_| |_| |_|___/    |                                                    
   __                                _   _____            _                  |
  /__\ ___ _ __ ___   _____   ____ _| | /__   \___   ___ | |                 |
 / \/// _ \ '_ ` _ \ / _ \ \ / / _` | |   / /\/ _ \ / _ \| |                 |
/ _  \  __/ | | | | | (_) \ V / (_| | |  / / | (_) | (_) | |                 |
\/ \_/\___|_| |_| |_|\___/ \_/ \__,_|_|  \/   \___/ \___/|_|                 |
                                                                             |
-----------------------------------------------------------------------------+
Title  : Neopets Valueless Items Removal Tool
Author : William Schneider (/u/wschneider)
Email  : willschneider (DOT) 513+VI (AT) gmail (DOT) com
Website: sourceflame.com
Purpose: To assist neopets users with the removal of valueless items from their
         Inventories. 

Disclaimers:
	 This script serves to assist users in discarding "valueless" items from
	 their neopets inventories by highlighting such items on the "quickstock" 
	 page. This is NOT in violation of the Terms of Use as of (3 February 2014)
	 If at any point this changes, I do not condone the use of this script. 

	 NEOPETS and all related indicia are trademarks of Neopets, Inc., © 1999-2014.

	 I am not affiliated with Neopets, Nickelodeon, Viacom, or any of the 
	 associated companies. 

Instructions:
	 (1) Prerequisites:
	     (*) Python 2.7 or later [[If you have no desire to update the items 
		                              in the list, this is not necessary]]
             (*) Google Chrome 
             (+) This application was designed for Windows 7, but should theoretically 
		 run on other systems that meet the above requirements
         (2) Assumptions:
             This tool assumes you have some working knowledge of how Chrome extensions 
	     work, how to at least read python and javascript code, and how to manage 
             files. 
	 (3) Running this program:
             (Step 0): If you are reading this file, you have either found, or downloaded 
		       the codes from github. If not, you will want to visit the website 
		       listed below and click the "Download Zip" button on the lower right
		       side. Unpack it somewhere on your computer
		            https://github.com/wschneider/ValuelessItems

	     (Step 1): If you are adding your own items to the list of items, continue with 
		       this step. If you are not, proceed to step 2. Open "itemsheet.csv" 
		       with your favorite spreadsheet editor (or text editor, that works too)
		       At the very end of the list, you can add any items you wish (as long 
		       as they are formatted so that one is on each line). When you save it
		       you MUST be sure to save it as "itemsheet.csv". Once you have saved it
		       run the script "genscript.py", which will generate a new "highlight.js" 
		       file. This file is your chrome extension.

	     (Step 2): Now you either have a self-generated (from Step 1) or the packaged 
		       "highlight.js" file. Open Google Chrome, and go to "chrome://extensions/"
		       where you should select the "Load Unpacked Extension..." option. 
		       Navigate to where you unpacked the directory where you unpacked the 
		       download, and click "Ok".

	     (Step 3): Go to "http://www.neopets.com/quickstock.phtml". Any items that were listed
		       in "itemsheet.csv" should be highlighted in green. As an economist, I
		       recommend whole-heartedly that you discard these items, but do as you
		       wish. Good Luck!


