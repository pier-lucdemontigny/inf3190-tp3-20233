document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('adoptionForm');
    const submitButton = document.getElementById('soumission');

    form.addEventListener('change', function (event) {
        switch (event.target.id) {
            case 'nom':
                validateNom();
                break;
            case 'espece':
                validateEspece();
                break;
            case 'race':
                validateRace();
                break;
            case 'age':
                validateAge();
                break;
            case 'description':
                validateDescription();
                break;
            case 'courriel':
                validateCourriel();
                break;
            case 'adresse':
                validateAdresse();
                break;
            case 'ville':
                validateVille();
                break;
            case 'cp':
                validateCp();
                break;
        }
    });

    submitButton.addEventListener('click', function (event) {
        if (!validateForm()) {
            event.preventDefault();
        }
    });

    function validateNom() {
        const field = document.getElementById('nom');
        const errorMessageElement = document.getElementById('erreurNom');
        const fieldName = 'Nom';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } else if (field.value.length < 3 || field.value.length > 20) {
            displayError(errorMessageElement, `Le nom de l'animal doit avoir entre 3 et 20 caractères.`);
            return false;
        } else if (/\d/.test(field.value)) {
            displayError(errorMessageElement, `${fieldName} ne doit pas contenir de chiffre.`);
            return false;
        }
    
        return true;
    }
    
    function validateEspece() {
        const field = document.getElementById('espece');
        const errorMessageElement = document.getElementById('erreurEspece');
        const fieldName = 'Espèce';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } else if (/\d/.test(field.value)) {
            displayError(errorMessageElement, `${fieldName} ne doit pas contenir de chiffre.`);
            return false;
        }
    
        return true;
    }

    function validateRace() {
        const field = document.getElementById('race');
        const errorMessageElement = document.getElementById('erreurRace');
        const fieldName = 'Race';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } else if (/\d/.test(field.value)) {
            displayError(errorMessageElement, `${fieldName} ne doit pas contenir de chiffre.`);
            return false;
        }
    
        return true;
    }
    
    function validateAge() {
        const field = document.getElementById('age');
        const errorMessageElement = document.getElementById('erreurAge');
        const fieldName = 'Âge';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } else if (isNaN(field.value) || field.value < 0 || field.value > 30) {
            displayError(errorMessageElement, `L'âge doit être une valeur numérique entre 0 et 30.`);
            return false;
        }
    
        return true;
    }
    
    function validateDescription() {
        const field = document.getElementById('description');
        const errorMessageElement = document.getElementById('erreurDesc');
        const fieldName = 'Description';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        }
    
        return true;
    }
    
    function validateCourriel() {
        const field = document.getElementById('courriel');
        const errorMessageElement = document.getElementById('erreurCourriel');
        const fieldName = 'Courriel';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } else {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(field.value)) {
                displayError(errorMessageElement, `L'adresse courriel doit avoir un format valide.`);
                return false;
            }
        }
    
        return true;
    }
    
    function validateAdresse() {
        const field = document.getElementById('adresse');
        const errorMessageElement = document.getElementById('erreurAdresse');
        const fieldName = 'Adresse';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        }
    
        return true;
    }
    
    function validateVille() {
        const field = document.getElementById('ville');
        const errorMessageElement = document.getElementById('erreurVille');
        const fieldName = 'Ville';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } 
    
        return true;
    }

    function validateCp() {
        const field = document.getElementById('cp');
        const errorMessageElement = document.getElementById('erreurCode');
        const fieldName = 'Code postal';
    
        clearError(errorMessageElement);
    
        if (!field.value.trim()) {
            displayError(errorMessageElement, `${fieldName} est obligatoire.`);
            return false;
        } else if (field.value.includes(',')) {
            displayError(errorMessageElement, `${fieldName} ne peut pas contenir une virgule.`);
            return false;
        } else {
            const postalCodeRegex = /^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$/;
            if (!postalCodeRegex.test(field.value)) {
                displayError(errorMessageElement, `Le code postal doit avoir un format canadien.`);
                return false;
            }
        }
    
        return true;
    }

    function validateForm() {
        let isValid = true;
    
        isValid = validateNom() && isValid;
        isValid = validateEspece() && isValid;
        isValid = validateRace() && isValid;
        isValid = validateAge() && isValid;
        isValid = validateDescription() && isValid;
        isValid = validateCourriel() && isValid;
        isValid = validateAdresse() && isValid;
        isValid = validateVille() && isValid;
        isValid = validateCp() && isValid;
    
        return isValid;
    }

    function displayError(errorMessageElement, message) {
        errorMessageElement.textContent = message;
        errorMessageElement.classList.add('message-erreur');
    }

    function clearError(errorMessageElement) {
        errorMessageElement.textContent = '';
        errorMessageElement.classList.remove('message-erreur');
    }
});