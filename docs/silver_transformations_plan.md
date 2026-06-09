# Silver Layer Transformation Plan

## Tables Processed

1. customers
2. orders
3. order_items
4. payments
5. products

---

## Transformation Strategy

- Read Bronze Delta tables
- Standardize schema
- Rename columns
- Cast data types
- Validate data quality
- Remove duplicates
- Write Silver Delta tables

---

## Data Quality Framework

### Critical Checks

- Null primary keys
- Null foreign keys
- Schema validation

### Warning Checks

- Invalid values
- Missing business attributes
- Invalid categorical values

---

## Duplicate Handling

| Table | Business Key |
|---------|---------|
| customers | customer_id |
| orders | order_id |
| products | product_id |
| payments | order_id, payment_sequential |
| order_items | order_id, order_item_id |

---

## Audit Logging

Audit logs are generated for:

- Null validations
- Duplicate validations
- Invalid value validations
- Severity level
- Failed record counts

Audit logs are stored in Delta format within the Audit container.

---

## Technologies

| Component | Technology |
|---|---|
| Processing | Azure Databricks |
| Transformation | PySpark |
| Storage | ADLS Gen2 |
| Format | Delta Lake |
| Orchestration | Azure Data Factory |

---

## Future Enhancements

- Incremental processing
- Data contracts
- Great Expectations integration
- Schema drift handling