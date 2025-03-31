# 📌 Documentación de Comandos .NET

## 1️⃣ Verificar la versión de .NET
Para comprobar la versión de .NET instalada en tu sistema, usa el siguiente comando:

```sh
dotnet --version
```

### 🔹 Explicación:
- Este comando devuelve la versión actual de **.NET SDK** instalada en el sistema.
- Es útil para asegurarte de que estás utilizando la versión correcta antes de compilar o ejecutar proyectos.

---

## 2️⃣ Compilar un proyecto .NET
Para compilar un proyecto en .NET, usa:

```sh
dotnet build
```

### 🔹 Explicación:
- Compila la aplicación y genera los archivos binarios en la carpeta **bin/**.
- Verifica que no haya errores en el código antes de la ejecución.
- Si el proyecto tiene dependencias, las restaura automáticamente.
- Genera un **archivo ejecutable** dentro de `bin/Debug/netX.X/` (según la versión de .NET que estés usando).

---

## 3️⃣ Ejecutar una aplicación .NET
Para ejecutar un proyecto en .NET, usa:

```sh
dotnet run
```

### 🔹 Explicación:
- Este comando compila y ejecuta la aplicación en un solo paso.
- Es ideal para desarrollo, ya que permite probar rápidamente el código sin necesidad de compilar manualmente.
- Si el código ya está compilado, ejecuta directamente el **binario** generado en `bin/Debug/netX.X/`.

---

## ✅ Verificación y Buenas Prácticas
- Antes de ejecutar `dotnet build` o `dotnet run`, asegúrate de estar en la carpeta raíz del proyecto.
- Usa `dotnet --version` si tienes problemas de compatibilidad con versiones de .NET.
- Para un mejor rendimiento en producción, usa `dotnet publish` en lugar de `dotnet run`.

## Ejecusion
- Abrir esta url en el navegador, tener en cuenta que puede trabajar en otro puerto.
```
http://localhost:5094/Calculator/
```

🚀 **¡Listo! Ahora puedes trabajar con .NET de manera eficiente.**

---

📌 **Autor:** Gaston Quelali

