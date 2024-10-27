'''Pour chaque ligne dans Orders_table :
    Créer un document 'order' :
        - orderNumber
        - orderDate
        - requiredDate
        - shippedDate
        - status
        - comments
    
    Pour chaque ligne dans OrderDetails_table oÃ¹ OrderDetails_table.orderNumber = Orders_table.orderNumber :
        Créer une sous-collection 'OrderDetails' :
            - quantityOrdered
            - priceEach
            - orderLineNumber

        Pour chaque ligne dans Products_table oÃ¹ Products_table.productCode = OrderDetails_table.productCode :
            Imbriquer les informations du produit :
                - productCode
                - productName
                - productLine
                - productScale
                - productVendor
                - productDescription
                - quantityInStock
                - buyPrice
                - MSRP
            Fin pour

    Fin pour (OrderDetails)

    Pour chaque ligne dans Customers_table oÃ¹ Customers_table.customerNumber = Orders_table.customerNumber :
        CrÃ©er une sous-collection 'Customers' :
            - customerName
            - contactLastName
            - contactFirstName
            - phone
            - addressLine1
            - addressLine2
            - city
            - state
            - postalCode
            - country
            - salesRepEmployeeNumber
            - creditLimit

        Pour chaque ligne dans Payments_table oÃ¹ Payments_table.customerNumber = Customers_table.customerNumber :
            CrÃ©er une sous-collection 'payments' :
                - checkNumber
                - paymentDate
                - amount
            Fin pour (Payments)

    Fin pour (Customers)

    Ajouter le document 'order' Ã  la collection NoSQL 'Orders'
Fin pour (Orders_table)


Pour chaque ligne dans Employees_table :
    CrÃ©er un document 'employee' :
        - employeeNumber
        - lastName
        - firstName
        - extension
        - email
        - reportsTo
        - jobTitle

    Pour chaque ligne dans Offices_table oÃ¹ Offices_table.officeCode = Employees_table.officeCode :
        Imbriquer les informations du bureau :
            - officeCode
            - city
            - phone
            - addressLine1
            - addressLine2
            - state
            - country
            - postalCode
            - territory
        Fin pour (Offices)

    Ajouter le document 'employee' Ã  la collection NoSQL 'Employees'
Fin pour (Employees_table)

'''
