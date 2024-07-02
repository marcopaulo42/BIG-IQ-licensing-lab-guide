.. _unmanaged-change:

Exercise 2: Unmanaged Device License Change
===========================================

.. important:: Complete :ref:`Exercise 1<unmanaged-change>` first.

#. In the BIG-IQ GUI, navigate to **License Management >> Assignments** on the **Devices** tab. Check the box next to
   the assignment for ``BIG-IP 1`` at 10.1.1.5. Click **Change License**.

   .. image:: ../images/big-iq-assignments.png

#. On the **Change License** screen, assign a new license from the **F5-BIG-MSP-BT-1G-LIC-DEV** offering using the
   following parameters, and then click **Assign**:

   * **Username:** admin
   * **Password:** !f5admin
   * **License Type:** Utility
   * **Name:** LOADV4
   * **Offering:** F5-BIG-MSP-BT-1G-LIC-DEV
   * **Unit of Measure:** Yearly

   .. image:: ../images/big-iq-chg-lic.png

#. Click **OK** in the popup confirmation window to apply the new license.

   .. warning:: Changing the license on an active BIG-IP will disrupt traffic processing.

#. Wait a few minutes for ``BIG-IP 1`` to apply the license, and then login to its GUI using the admin credentials
   (admin/!f5admin). Navigate to **System >> License**.

   Notice the licensed active modules now reflects a Best license.

   .. image:: ../images/big-ip-lic-best.png
