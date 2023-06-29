Exercise 1: Enabling Report Generation
======================================

BIG-IQ supports automatic report generation with both automatic and manual submission.

To configure automatic report generation with automatic submission:

#. In the BIG-IQ GUI, navigate to the **Devices** tab and then to **License Management >> Reporting** using the left
   navigation column.

   .. image:: ../images/lm-reports.png

#. Click **Schedule**.

#. Configure reporting as follows:

   * **Schedule Status:** Enable
   * **Submission Method:** Automatically submit report to F5
   * **Day/Time:** Day - 1, Hour - 0, Minute - 0
   * **Obfuscate Data:** No
   * **Email Notification:** Disable (leave unchecked)

   .. image:: ../images/lm-reports-schedule.png

   .. tip:: Reports are typically sent on the first day of the month. Consider setting a custom time to avoid peak
      traffic at the start of each hour.

#. Click the blue **Save & Close** button.

.. _autoreportnotes:
.. seealso::
   `K15202: IP addresses for F5 hosted services <https://my.f5.com/manage/s/article/K15202>`_
      IP address ranges for ``api.f5.com`` where automatic usage reports are sent.

   `K33302139: "General SSLEngine problem" error when uploading qkviews to iHealth on a BIG-IQ <https://my.f5.com/manage/s/article/K33302139>`_
      Discusses how to add a CA certificate to BIG-IQ if a proxy server or security device is intercepting calls to
      ``api.f5.com``.
