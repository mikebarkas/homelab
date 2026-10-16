-- Issue #32: store timestamp as timestamptz (UTC) and reject duplicate rows.
-- Run once, before deploying the stocker image that uses "on conflict".
-- Back up first: pg_dump -t stock stocker > stock-backup.sql

-- Preview rows that will be removed:
-- select * from stock
-- where symbol is null or current is null or "timestamp" is null
--    or "timestamp" = '' or "timestamp" like '1970-%';
--
-- select symbol, "timestamp", count(*) from stock
-- group by 1, 2 having count(*) > 1;

begin;

-- rows with missing data, or a t=0 result (written as 1970)
delete from stock
where symbol is null or current is null or "timestamp" is null
   or "timestamp" = '' or "timestamp" like '1970-%';

-- keep one row per (symbol, timestamp)
delete from stock a using stock b
where a.ctid > b.ctid
  and a.symbol = b.symbol
  and a."timestamp" = b."timestamp";

-- existing text is UTC with no offset; read it as UTC, not the session time zone
alter table stock
  alter column "timestamp" type timestamptz
  using ("timestamp"::timestamp at time zone 'UTC');

alter table stock
  add constraint stock_symbol_timestamp_key unique (symbol, "timestamp");

commit;
