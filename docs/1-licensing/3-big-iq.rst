.. _3-bigiq_setup:

Exercise 2: BIG-IQ Setup and Activation
=======================================

#. Access the BIG-IQ Graphical User Interface (GUI) via the UDF Web console, by selecting the **Components** tab, then selecting **Access** on the BIG-IQ F5 Products Tile, and then click the **TMUI** link on the dropdown.

   .. image:: ../images/big-iq-access.png

#. Login as ``admin`` using the default credentials:

   * **Username:** admin
   * **Password:** default

#. You will need to immediately update the password. Enter ``default`` as the current password and enter ``!f5bigiqadmin`` as the new password for this lab.
   Complete the form, and then click **Save**.

   You will be redirected back to the login page. Login with the updated credentials.

   * **Username:** admin
   * **Password:** !f5bigiqadmin

#. The BIG-IQ Setup wizard will launch. The first step is licensing. 

   Select the **License** radio button on the **License Information** page. 
   From the Email received for the **F5 Product: F5-BIQ-VE-LIC-MGR-LIC-DEV**, copy the corresponding **Registration Key**, and paste this into the **Base Registration Key** field.
   Select the **Automatic** radio button and then click **Activate**. Click **Agree** on the EULA pop-up.
   If the activation was successful, a line indicating *License activation completed successfully.* will appear on the page.
   
   Click the blue **Next** button to continue.

    .. image:: ../images/big-iq-lic-auto.png   

#. **Optional: Manual Activation**
   
   .. note:: 
      If you wish to experience the **Manual Activation** procedure, perform the following optional Manual    Activation Step.

   The Manual Activation method can be performed for the case of activating the BIG-IQ that does not have internet access to the F5 License Servers.
   Select **Manual** for the **Activation Method**. Then click the **Get Dossier** button.

   .. image:: ../images/lm-license-activation.png

   Copy the dossier text and navigate to the `Dev Key Activation <https://license.f5net.com/license/dossier.jsp>`_ page.
   Complete the prompts and copy the returned license text to the **License Text** field in BIG-IQ. Then click
   **Activate**. The text *"License activation completed successfully."* should appear next to the Activate button.
   Click the blue **Next** button to continue.

#. Create a **Master Key**. Use ``!F5abcdefghijklm`` for this lab. Click the blue **Next** button.

   .. important:: Retain this key and treat it like a password. You will need it if you decide to implement HA.

#. On the screen *Update Account Passwords* Update the root password. Use ``!f5bigiqroot`` for this lab. This password is used to access the **root** user via the Command Line Interface (CLI) . Click the blue **Next** button.

   .. image:: ../images/root-passwd.png

#. On the *System Personality* screen, **BIG-IQ Central Management** is preselected and cannot be changed. Click
   **Next**.

   .. image:: ../images/system-personality.png

   .. attention:: You cannot change the System Personality. This is a known issue. Only the license management features
      of BIG-IQ are enabled when a LM key is used to activate BIG-IQ.

#. On the *Networking* screen, set a system hostname. Use ``bigiq.example.lan`` for this lab. Self IPs are not
   required when BIG-IQ is only used for license management. Click the blue **Next** button.

   .. note:: For the BIG-IQ *Hostname*, you must use a `fully qualified domain name <https://en.wikipedia.org/wiki/Fully_qualified_domain_name>`_.

#. Review the DNS and NTP settings on the *Services* screen. Change the *Time Zone* to match your region. Click the blue **Next** button.

   .. tip:: Both DNS and NTP servers should be configured in customer environments, especially if automatic license
      activation is used.

#. Review the configured settings on the *Summary* screen. Click the blue **Launch** button. Click **Restart** on the
   popup window. The services will restart while bootstrap logs scroll across the screen.

   .. image:: ../images/restart-services.png

   Bootstrapping should complete in 5-10 minutes. Your session will automatically terminate and you will be redirected to the
   login screen while services continue to restart. (Please note that this can take a few minutes).

   .. image:: ../images/restart-services-login.png

#. Use the previously created credentials:

   * **Username:** admin
   * **Password:** !f5bigiqadmin
   
   to login, and continue to the next exercise.
