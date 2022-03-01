## MongoDB tasks

### Task 1.

The 'Account' collection contains documents of the form:

    {
        'number': '7800000000000',
        'name': 'Пользователь №',
        'sessions': [
            {
                'created_at': ISODate('2016-01-01T00:00:00'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': ISODate('2016-01-01T01:20:01'),
                    },
                    {
                        'type': 'read',
                        'created_at': ISODate('2016-01-01T01:21:13'),
                    },
                    {
                        'type': 'create',
                        'created_at': ISODate('2016-01-01T01:33:59'),
                    }
                ],
            }
        ]
    }

   It is necessary to write an aggregation query that will display the last action for each user
   and the total for each of the 'actions' types. The final data should be in the form of a list of documents:

    {
        'number': '7800000000000',
        'actions': [
            {
                'type': 'create',
                'last': 'created_at': ISODate('2016-01-01T01:33:59'),
                'count': 12,
            },
            {
                'type': 'read',
                'last': 'created_at': ISODate('2016-01-01T01:21:13'),
                'count': 12,
            },
            {
                'type': 'update',
                'last': null,
                'count': 0,
            },
            {
                'type': 'delete',
                'last': null,
                'count': 0,
            },
        ]
    }
    
    
### Task 2.

There are two collections (tables) of data: accrual (debts) and payment (payments). Both collections have fields:
- id
- date 
- month 

It is necessary to write a function that will make a request for payments and find for each payment the debt that will be paid by them. A payment can only pay off a debt that has an earlier date. One payment can only pay one debt, and each debt can only be paid in one payment. The payment must first select a debt with the same month (field month). If there is none, then the oldest by date (date field) debt.
The result should be a table of found matches, as well as a list of payments that did not find a debt.
The query can be made to any database (mongodb, postgresql or others) in any way.

