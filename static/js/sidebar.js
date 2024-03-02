
        // Obtener todos los botones
        var botones = document.querySelectorAll(".boton");
        
        // Agregar el evento 'click' a cada botón
        botones.forEach(function(boton) {
          boton.addEventListener("click", function() {
            // Iterar sobre cada botón y remover la clase 'selected'
            botones.forEach(function(boton) {
              boton.classList.remove("selected");
            });
            // Agregar la clase 'selected' solo al botón actual
            this.classList.add("selected");
          });
        });
    