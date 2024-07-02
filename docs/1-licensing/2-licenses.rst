.. _2-licenses:

Exercise 1: Obtaining Licenses
==============================

Two licenses are required: one for BIG-IQ License Manager (LM), and one Catalog (CAT) or Load (LOAD) key. Keys were not
pre-provisioned in this lab because they do not offer the Recycle bit.

#. Connect to the VPN. Navigate to the `F5 Licensing Tools <https://license.f5net.com/devkeygenerator/home.jsp>`_ site,
   and then click on the **Dev Key Generator** link.

   .. tip:: You can also access this site using `Federate <https://federate.f5.com>`_.

#. Generate a License Manager license using the following selectors:

   * **Product Line:** BIG-IQ
   * **Platform:** VE
   * **Part Number:** F5-BIQ-VE-MAX-LIC-DEV
   * **EULA:** Select

   .. image:: ../images/lm-license-gen.png

#. Complete the workflow by clicking **Next >>** twice.

#. Click **Generate A New Key** or **Generate Another Key**.

#. Generate a LOAD Base Registration key using the following selectors:

   * **Product Line:** BIG-IP
   * **Platform:** VE
   * **Part Number:** F5-BIG-MSP-LOADV4-LIC-DEV
   * **EULA:** Select

   .. image:: ../images/cat-license-gen.png

   .. attention:: The Dev Key Generator does not include CAT Base Registration Key licenses.
#. Click **Home** on the top page navigator

   .. image:: ../images/Home.png

#. On the **F5 Licensing Tools** page, click on the **Eval Key Generator** link.

#. Generate a CAT Base Registration key using the following selectors:

   * **Product Line:** BIG-IP
   * **Platform:** VE-Catalog
   * **Part Number:** F5-BIG-CAT-A-1-LIC

   .. image:: ../images/CAT-Regkey.png

#. Complete the workflow by clicking **Next >>** twice.

#. Click **Next ->** to continue to the next exercise once you receive these keys via your corporate email (this should takes a few minutes to arrive after successful generation).
