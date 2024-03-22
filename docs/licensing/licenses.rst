.. _licenses:

Exercise 1: Obtaining Licenses
==============================

Two licenses are required: one for BIG-IQ License Manager (LM), and one Catalog (CAT) or Load (LOAD) key. Keys were not
pre-provisioned in this lab because they do not offer the Recycle bit.

#. Connect to the VPN. Navigate to the `F5 Licensing Tools <https://license.f5net.com/devkeygenerator/home.jsp>` site,
   and then click on the Dev Key Generator link.

   .. tip:: You can also access this site using `Federate <https://federate.f5.com>`_.

#. Request a License Manager license using the following selectors:

   * **Product Line:** BIG-IQ
   * **Platform:** VE
   * **Part Number:** F5-BIQ-VE-LIC-MGR-LIC-DEV

   .. image:: ../images/lm-license-gen.png

#. Complete the workflow and return to the Dev Key Generator to request a CAT key.

#. Request a CAT key using the following selectors:

   * **Product Line:** BIG-IP
   * **Platform:** VE
   * **Part Number:** F5-BIG-MSP-LOADV4-LIC-DEV

   .. image:: ../images/cat-license-gen.png

   .. attention:: The Dev Key Generator does not include CAT licenses. For this lab we will use older
      LOAD licenses which offer similar functionality.

#. Continue to the next exercise once you receive your keys.
