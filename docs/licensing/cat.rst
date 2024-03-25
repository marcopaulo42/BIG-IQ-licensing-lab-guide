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

#. From the Email received for the F5 Product: F5-BIG-MSP-LOADV4-LIC-DEV, copy the corresponding Registration Key and use this to complete the *Add and Activate New License* fields as follows:

   * **License Name:** LOADV4
   * **Base Registration Key:** <obtained from email>
   * **Activation Method:** Manual

   .. image:: ../images/cat-license-add.png

   .. tip:: The *License Name* can be changed later.

#. Click **Generate Dossier**. Copy the dossier text and navigate to the `Dev Key Activation
   <https://license.f5net.com/license/dossier.jsp>`_ page. Agree to the EULA, clicke *Next*. Copy the returned license text to the **License Text** field. Click the blue **Activate** button on the bottom right of the screen.

#. You will be redirected to the *Licenses* page and the ``LOADV4`` license should be in **Pending** status.

   .. image:: ../images/cat-license-pending.png

#. Click on ``LOADV4`` to review the license's properties.

   The top portion of the page displays information about the Base Registration license.

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

#. You will return to the *Licenses* page. Note that the offering now has a an **Active** status with a Green dot next to it. In the *Filtered by:* window, click the small **x** on the right hand side of the text box to restore the full list of offerings for this Base Registration key.

   .. image:: ../images/filtered-by-x.png

   .. tip:: In a real environment, the remaining *Pending* offerings in this list must be manually activated. This is why Automatic Activation is *strongly* encouraged. This also reduces the risk of Copy - Paste errors.
   .. tip:: The *Description* field of each offering is editable. One suggestion is to use this field to enter a description of each Offering Name. Make sure to click the **Save & Close** button to save any edits.
