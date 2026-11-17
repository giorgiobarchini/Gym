# Cuaderno de Gym con Supabase

Así la app queda como una app propia en el teléfono, con tu ícono, a pantalla completa y con los datos guardados en tu propia base de Supabase.

Hay tres partes:

1. **Supabase:** la base de datos y el login.
2. **GitHub Pages:** dónde vive la app, gratis.
3. **El teléfono:** instalar el ícono.

---

## 1. Supabase (10 minutos)

1. Entrá a <https://supabase.com>, creá una cuenta y un proyecto nuevo (**New project**). Elegí la región más cercana, por ejemplo São Paulo. Guardá la contraseña de la base en algún lado; la app no la usa.
2. Cuando el proyecto esté listo, andá a **SQL Editor → New query**, pegá todo el contenido de [`supabase/schema.sql`](supabase/schema.sql) y tocá **Run**. Tiene que decir "Success".
3. Andá a **Authentication → Sign In / Providers → Email**:
   - Dejá **Email** activado.
   - Recomendado: desactivá **Confirm email**. Así creás la cuenta desde la app y entrás directo, sin tener que abrir un mail.
4. Andá a **Project Settings → API** (o **API Keys**) y copiá estos dos datos:
   - **Project URL**: algo como `https://abcdefgh.supabase.co`
   - La clave **anon** o **publishable**: una cadena larga.

   ⚠️ **No copies la clave `service_role` ni la `secret`.** Esa nunca va en la app.

Pasame esos dos datos y yo los pongo en `docs/config.js`. También los podés pegar vos ahí.

> La clave anon/publishable es pública por diseño: va dentro de la app y cualquiera podría verla. Lo que protege tus datos son las reglas (RLS) que crea `schema.sql`: cada usuario solo puede leer y escribir sus propias filas.

5. **Después de crear tu cuenta desde la app**, volvé a **Authentication → Sign In / Providers** y desactivá **Allow new users to sign up**. Así nadie más puede crearse una cuenta en tu app.

---

## 2. GitHub Pages (5 minutos)

La app ya está armada en la carpeta `docs/` del repo.

1. En GitHub, abrí el repo **Gym → Settings → Pages**.
2. En **Build and deployment → Source** elegí **Deploy from a branch**.
3. En **Branch** elegí `claude/kind-bohr-mv2nic` y la carpeta **`/docs`**. Tocá **Save**.
   - Si más adelante pasás todo a `main`, cambiá esto a `main` y `/docs`.
4. En uno o dos minutos aparece la dirección. Va a ser algo como `https://giorgiobarchini.github.io/Gym/`.

> **Si el repo es privado:** GitHub Pages en repos privados solo está en los planes pagos. Tenés dos opciones:
> - **Hacer el repo público.** En el código no hay nada secreto.
> - **Usar otro servicio gratis** como Netlify, Vercel o Cloudflare Pages, apuntando a la carpeta `docs/`.

Opcional: en Supabase, en **Authentication → URL Configuration**, poné esa dirección como **Site URL**.

---

## 3. Instalar en el teléfono

**iPhone (tiene que ser Safari):**

1. Abrí la dirección de GitHub Pages.
2. Tocá compartir (el cuadrado con la flecha).
3. Elegí **Agregar a pantalla de inicio**.

**Android (Chrome):**

1. Abrí la dirección.
2. Tocá ⋮.
3. Elegí **Instalar app** o **Agregar a la pantalla principal**.

Abrí la app desde el ícono, tocá **"No tengo cuenta: crear una"**, poné tu email y una contraseña, y listo. Quedás logueado; no te la vuelve a pedir.

---

## Cómo funciona

- **`index.html` es la fuente única.** Es la misma app que se publica en Claude.
- **`python3 tools/build_pages.py`** arma la versión instalable en `docs/`: le agrega el ícono, el manifest y Supabase.
- **`python3 tools/make_icons.py`** genera los íconos.
- **Los datos** se guardan en la tabla `gym_docs`: una fila por cosa (ajustes, cada día, cada peso, cada entrenamiento), siempre ligada a tu usuario. También queda una copia en el teléfono, por si no hay señal en el gym; se sincroniza cuando vuelve la conexión o cuando volvés a abrir la app.
- **En esta versión no están el coach ni el "¿Qué cocino?",** porque esos usan Claude y solo funcionan en la versión publicada en Claude.
