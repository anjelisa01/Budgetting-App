
### Database Schema Summary

This database schema is for a **personal finance app** which allows users to manage their accounts, track transactions, create budgets for their categories, and set financial goals.

The core entity is the **`users`** table, which stores user information such as name, email, password, currency, and account creation details. Each user can have multiple financial accounts, categories, and goals.

The **`accounts`** table stores users' financial accounts, including account names and current balances. Each account belongs to a one user and is used to record financial activities through transactions.

The **`transactions`** table records all financial activities, including income and expenses. Each transaction contains details such as title, amount, notes, transaction type, creation date, associated account, and optional category. Transactions are linked to an account and can be assigned to a category.

The **`category`** table is used to classify transactions into different groups, for example user can create categories such as food, transportation, or entertainment. Each category belongs to a specific user.

The **`budget`** table defines spending limits for specific categories. Each budget is associated with one category and includes the maximum allowed amount and the budget period, which can be daily, weekly, or monthly.

The **`goals`** table stores users' financial goals, such as saving targets. It includes information about the goal name, target amount, saved amount, deadline, and the account used for saving.

The schema has two enums:

* **`period`**: Defines the budget duration options (`daily`, `weekly`, `monthly`).
* **`transaction_type`**: Defines transaction classifications (`income` or `expense`).

### Relationships Overview:

* One **user** can have many **accounts**, **categories**, and **goals**.
* One **account** can contain many **transactions**.
* One **category** can be linked to many **transactions** and one **budget**.
* Each **transaction** belongs to one account and may optionally belong to one category.
* Each **goal** is connected to both a user and an account.
