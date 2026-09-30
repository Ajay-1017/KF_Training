# Choosing Between ON DELETE CASCADE and ON DELETE SET NULL

The choice between **`ON DELETE CASCADE`** and **`ON DELETE SET NULL`** depends entirely on the **lifecycle and relationship** between your database tables. Use `CASCADE` when the child row cannot exist without its parent, and use `SET NULL` when the child row remains meaningful even after the parent is deleted.

---

## Quick Comparison

| Feature | `ON DELETE CASCADE` | `ON DELETE SET NULL` |
| :--- | :--- | :--- |
| **Action** | **Deletes** all related child rows automatically. | **Keeps** the child rows but sets the foreign key column to `NULL`. |
| **Child Ownership** | The child is strictly owned by the parent (identifying relationship). | The child can exist independently of the parent. |
| **Column Requirement** | The Foreign Key column can be `NOT NULL`. | The Foreign Key column **must allow `NULL` values**. |
| **Risk Factor** | **High.** Can trigger a chain reaction that deletes massive amounts of data. | **Low.** Retains data history but creates "orphan" records. |

---

## When to Use `ON DELETE CASCADE`

Use this option when a child row is a **direct component or extension** of the parent. If the parent is removed, the child row becomes completely useless metadata.

### Common Examples:
* **Orders and Order Items:** If you delete an `Order`, the `Order_Items` (the products bought in that specific transaction) have no reason to remain in the database.
* **User Accounts and Profiles:** If a user deletes their `Account`, their corresponding `User_Profile` or `Account_Settings` row should be purged immediately.
* **Blog Posts and Comments:** If a `Blog_Post` is deleted, all `Comments` attached to that post should automatically vanish.

---

## When to Use `ON DELETE SET NULL`

Use this option when the child row represents an **independent entity** that should be preserved for historical tracking, auditing, or reassignment.

### Common Examples:
* **Departments and Employees:** If a `Department` is dissolved, you don't want to fire the `Employees`. Instead, you set their `department_id` to `NULL` until they are reassigned.
* **Products and Categories:** If you delete a product `Category` (e.g., "Summer Clearance"), the actual physical `Products` shouldn't be deleted. They simply become uncategorized (`category_id = NULL`).
* **Content and Authors:** If a freelance writer deletes their `Author` account, a news website will usually want to keep the written `Articles` online, simply marking the author field as `NULL` or "Anonymous".
