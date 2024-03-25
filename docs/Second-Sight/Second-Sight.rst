Module 4: Usage Telemetry Script (for Second Sight)
***************************************************

Second Sight is F5's business insights and visibility platform. To obtain usage data insights from Classic BIG-IQ a small script will need to be downloaded and installed on the customer's BIG-IQ Centralized Manager. (This script will not work on BIG-IQ License Manager).

For additional insights, each BIG-IP should have Application Visibility and Reporting (AVR) enabled, BIG-IQ CM should be connected to at least one DCD and stats collection should be enabled.

The script takes a few seconds to download from F5's GITHUB repository and less than 5 minutes to run on a network of 600 managed BIG-IP devices.

F5 requires the script is run once a month and the data file is emailed to their CSM, or group email address. BIG-IQ maintains reports about licenses it issues and revokes. These reports are used for both billing and reference.

For reference and more information, please see the Support Solution Article <https://my.f5.com/manage/s/article/K29144504>_


.. toctree::
   :maxdepth: 1
   :name: lab-setup-toc
   :glob:

   enabling
   manual
   historical

