Exercise 2: Manual Generation
=============================

.. tip:: License the BIG-IP before completing this exercise. See :ref:`Module 2 <assign_revoke>` for
   various ways to issue licenses.

Manual report generation may be required periodically, and is also useful for testing if
automatic report submission is correctly working.

#. On the **Devices** tab, navigate to **License Management >> Reports**. Click the **Generate** button.

#. Generate a **Utility Billing Report** with the following options:

   * **Type:** Utility Billing Report
   * **Licenses:** Click ``LOADV4`` then the right arrow button to move it to the *Selected* column.
   * **Submission Method:** Manual
   * **Obfuscate Data:** No

#. Click the **Download** button to download the JSON report. Then click **Cancel** to return to the previous screen.

#. The *Utility Billing* report should appear in the list of reports. If not, refresh the page.

   .. image:: ../images/lm-reports-ub.png

#. Check the box next to the report. Notice the **Download** and **Send To F5** buttons enable. It is possible to
   download the report again, as well as attempt to automatically submit a manually-generated report to F5.

.. important:: A *Utility Billing Report* only shows license activity since the last billing report was run. You cannot
   specify a timeframe for the report, nor can you regenerate reports for previous timeframes.
