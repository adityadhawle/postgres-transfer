# PostgreSQL Transfer Processor

## Difficulty explanation

This task requires implementing a transactional PostgreSQL transfer operation while preserving an existing Python interface. The main challenges are choosing the correct transaction boundary, ensuring rollback after a mid-operation failure, validating database state before mutation, handling insufficient funds, and making retries idempotent. An experienced Python/PostgreSQL developer should be able to complete the task in a focused session.

## Solution explanation

The reference solution validates the request before making changes, checks for an existing completed transfer, locks the relevant account rows, performs the debit, optional failure injection, credit, and transfer-record insertion inside one PostgreSQL transaction, and closes the connection even when an exception occurs.

## Verification explanation

The verifier executes the transfer implementation against PostgreSQL and checks successful transfers, rollback after a simulated failure, insufficient-balance handling, duplicate transfer IDs including concurrent retries, non-positive amounts, and missing source or destination accounts. It also verifies the resulting account balances and transfer records.

## Relevant experience

The author is a Data Engineer with professional experience building Python, SQL, ETL, and cloud data pipelines, including data validation and reliable batch processing.

## Change Log

- Initial task authoring and verifier setup.

