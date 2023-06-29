.. _unmanaged-revoke:

Exercise 3: Unmanaged Device License Revoke
===========================================

In this exercise, BIG-IQ revokes a license on a previously-licensed BIG-IP.

.. important:: Revoking a license is an important step to complete before decomissioning or deleting a BIG-IP and
   ensures usage reports are correctly updated.

#. In the BIG-IQ GUI, navigate to **License Management >> Assignments** on the **Devices** tab. Check the box next to
   the assignment for ``BIG-IP 1`` at 10.1.1.5. Click **Revoke**.

#. On the **Revoke Assignments** screen, enter the admin credentials for ``BIG-IP 1`` (admin/!f5admin), and then click
   **Revoke**.

#. Click **OK** in the popup confirmation window to revoke the license.

   .. warning:: Revoking a license from a BIG-IP immediately halts traffic processing.

#. You should automatically return to the **Assignments** page. The assignment no longer appears.
