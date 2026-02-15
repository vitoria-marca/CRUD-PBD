document.addEventListener('DOMContentLoaded', function() {
    const tipoSelect = document.querySelector('#id_tipo'); // ID do seu campo choices
    
    const medicoInline = document.querySelector('#medico-group');
    const enfermeiroInline = document.querySelector('#enfermeiro-group');
    const tecAdminInline = document.querySelector('#tec_admin-group');

    function toggleInlines() {
        const val = tipoSelect.value;

        [medicoInline, enfermeiroInline, tecAdminInline].forEach(el => {
            if (el) el.style.display = 'none';
        });

        if (val === 'Medico' && medicoInline) medicoInline.style.display = 'block';
        if (val === 'Enfermeiro' && enfermeiroInline) enfermeiroInline.style.display = 'block';
        if (val === 'Tec Administrativo' && tecAdminInline) tecAdminInline.style.display = 'block';
    }

    if (tipoSelect) {
        tipoSelect.addEventListener('change', toggleInlines);
        toggleInlines();
    }
});