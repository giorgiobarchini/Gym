-- Cuaderno de Gym: una tabla con todos tus datos (ajustes, días, pesos y entrenamientos).
-- Pegá todo esto en Supabase → SQL Editor → New query → Run.

create table if not exists public.gym_docs (
  user_id    uuid        not null default auth.uid() references auth.users (id) on delete cascade,
  id         text        not null,
  data       jsonb       not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  primary key (user_id, id)
);

-- Cada usuario ve y modifica solo sus propias filas.
alter table public.gym_docs enable row level security;

drop policy if exists "gym_docs: leer lo propio" on public.gym_docs;
drop policy if exists "gym_docs: crear lo propio" on public.gym_docs;
drop policy if exists "gym_docs: editar lo propio" on public.gym_docs;
drop policy if exists "gym_docs: borrar lo propio" on public.gym_docs;

create policy "gym_docs: leer lo propio" on public.gym_docs
  for select to authenticated using ((select auth.uid()) = user_id);
create policy "gym_docs: crear lo propio" on public.gym_docs
  for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "gym_docs: editar lo propio" on public.gym_docs
  for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "gym_docs: borrar lo propio" on public.gym_docs
  for delete to authenticated using ((select auth.uid()) = user_id);

grant select, insert, update, delete on public.gym_docs to authenticated;
revoke all on public.gym_docs from anon;
