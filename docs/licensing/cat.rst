.. _cat:

Exercise 3: LOAD / CAT License Activation
=========================================

This exercise goes through the process of loading and activating both LOAD and CAT BIG-IP Base Registration Keys. Although CAT Base Registration Keys are provided, it is useful to see how the CAT Base Registration keys replace the deprecated LOAD Base Registration keys.

#. In the BIG-IQ LM GUI, click on the **Devices** tab and navigate using the left hand index to **License Management >> Licenses**.

   .. image:: ../images/devices-tab.png

   .. image:: ../images/licenses-sidebar.png

#. Click **Add License**.

   .. attention:: Make sure to click *Add License*. Do not click *Add RegKey Pool*. This is very often where customers go wrong.

   .. image:: ../images/add-license.png

#. Complete the *Add and Activate New License* fields as follows:
From the Email received for the F5 Product: F5-BIQ-VE-LIC-MGR-LIC-DEV, copy the corresponding Registration Key, and paste this into the Base Registration Key field. Select the Automatic radio button and then click Activate. Click Agree on the EULA pop-up. If the activation was successful, a line indicating License activation completed successfully. will appear on the page.

Click the blue Next button to continue.

   * **License Name:** LOADV4
   * **Base Registration Key:** <obtain from email>
   * **Activation Method:** Manual

   .. image:: ../images/cat-license-add.png

   .. tip:: The *License Name* can be changed later.

#. Click **Generate Dossier**. Copy the dossier text and navigate to the `Dev Key Activation
   <https://license.f5net.com/license/dossier.jsp>`_ page. Copy the returned license text to
   the **License Text** field. Click **Activate**.

#. You will be redirected to the *Licenses* page and the ``LOADV4`` license should be in **Pending** status.

   .. image:: ../images/cat-license-pending.png

#. Click on ``LOADV4`` to review the license's properties.

   The top portion of the page displays information about the CAT license.

   * The *Name* field is editable.
   * The *Service Check Date* should be today. Every issued BIG-IP license inherits this date.
   * The *License Status* should say "Waiting For Offering License Texts."

   .. image:: ../images/cat-license-props.png

#. In the **Offerings** section, enter **F5-BIG-MSP-LTM-1G-LIC-DEV** into the **Filter** search box and
   press Enter. One entry should be returned. Click on the blue **F5-BIG-MSP-LTM-1G-LIC-DEV** link.

   .. image:: ../images/cat-ltm-1g.png

#. Copy the **Device Dossier** text and navigate to the `Dev Key Activation
   <https://license.f5net.com/license/dossier.jsp>`_ page again to activate the offering. Copy the returned license to
   **License Text** field, and then click on **Activate**.

   .. image:: ../images/cat-ltm-1g-activation.png

#. You will return to the *Licenses* page. Note that the offering is now **Active**. Click the small **x**
   next to the filter text to restore the full list of offerings. Then search for **F5-BIG-MSP-BT-1G-LIC-DEV** and
   activate it.

   .. image:: ../images/filtered-by-x.png

   .. tip:: In a real environment, all 37 offerings in this license must be activated. This is why
      automatic activation is *strongly* encouraged.

#. Use the **x** to remove the filter text, and then click on the **Status** column heading until the arrow points down
   and the activated offerings are shown. You should see the two active offerings.

   .. image:: ../images/cat-active-offerings.png

   .. tip:: The *Description* field of each offering is editable. Make sure to click the **Save & Close** button to save
      any edits.
