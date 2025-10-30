 // --- Lógica para la animación de scroll ---
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
                // Opcional: remover la clase si sale de la vista
                // else {
                //     entry.target.classList.remove('visible');
                // }
            });
        }, {
            threshold: 0.1 // Activar cuando el 10% del elemento sea visible
        });

        // Observar todos los elementos con la clase .reveal
        const revealElements = document.querySelectorAll('.reveal');
        revealElements.forEach(el => observer.observe(el));