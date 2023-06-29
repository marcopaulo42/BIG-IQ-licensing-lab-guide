.. _licuser:

Exercise 4: License Manager User Role (Optional)
================================================

BIG-IQ supports role-based access control (RBAC), and contains a built-in *License Manager* role which only authorizes
license management features. This optional exercise creates a user with the *License Manager* role and shows how the GUI
changes for such users.

#. Login to BIG-IQ as admin. On the **System** tab, navigate to **User Management >> Users**. Click the **Add**
   button.

#. Create a user for licensing with the following properties:

   * **Auth Provider:** local (Local)
   * **User Name:** licensing
   * **Full Name:** Licensing User
   * **Password** and **Confirm Password:** !f5licensing
   * **Roles:** Check the box next to **License Manager** and then click the right arrow button to move it to the
     *Selected* column.

   .. image:: ../images/add-user.png

#. Click **Save & Close** to return to the **Users** screen.

#. In the upper-right corner, click your user icon and select **Log out**.

   .. image:: ../images/log-out.png

#. Login as the *licensing* user.

   * **Username:** licensing
   * **Password:** !f5licensing

#. The user interface is simplified, with fewer tabs and left navigation menu choices.

   .. image:: ../images/big-iq-lic-user-gui.png
