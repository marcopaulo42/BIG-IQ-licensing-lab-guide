.. _unmanaged-licensing:

Exercise 1: Unmanaged Device Licensing
======================================

In this exercise, BIG-IQ assigns a license on a BIG-IP but does not manage the device's configuration.

#. Login to BIG-IQ and navigate to the **Licenses** screen on the **Devices** tab. Click on the ``LOADV4`` license
   link. Locate the **F5-BIG-MSP-LTM-1G-LIC-DEV** offering and click on it. You should see its properties page. Click on
   **License Devices**.

   .. image:: ../images/offering-props.png

#. License the ``BIG-IP 1`` VE using the following properties:

   * **Unit of Measure:** Yearly
   * **Device Address:** 10.1.1.5
   * **Port:** 443
   * **Username:** admin
   * **Password:** !f5admin

   Click **Assign** after filling in the fields.

   .. important:: The **Unit of Measure** is always **Yearly** for CAT licenses.

   .. tip:: The **Chargeback Tag** is customer-specified information (like department) associated with the assignment.

   .. image:: ../images/unmanaged-assign.png

#. Click **OK** in the popup window that appears asking you to confirm the assignment.

#. You should automatically return to the offering's properties page. The assignment now appears in the lower portion of
   the screen.

   .. image:: ../images/offering-props-with-assignment.png

   .. attention:: Observe that the **Device Name** is ``bigip1``. BIG-IQ obtains the BIG-IP's hostname once during
      licensing. If the hostname is updated, BIG-IQ will **not** reflect the change.

#. Login to the GUI for ``BIG-IP 1`` using the admin credentials (admin/!f5admin). Navigate to **System >> License**.

   Notice the **License Manager** line indicating the IP address of the BIG-IQ that provided the license. Also, observe
   the only active module is LTM.

   .. image:: ../images/big-ip-lic-ltm.png

   .. tip:: When opening support cases for a BIG-IP licensed through BIG-IQ, do not use any license key information from
      the BIG-IP. Instead, use the CAT key from BIG-IQ.
