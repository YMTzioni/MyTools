document.getElementById('passwordForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const password = document.getElementById('password').value;
    const feedback = document.getElementById('feedback');
    const result = checkPasswordStrength(password);
    feedback.innerHTML = `<strong>Strength:</strong> ${result.strength}<br><ul>${result.tips.map(tip => `<li>${tip}</li>`).join('')}</ul>`;
});

function checkPasswordStrength(password) {
    let score = 0;
    const tips = [];

    if (password.length >= 8) {
        score++;
    } else {
        tips.push('Use at least 8 characters.');
    }
    if (/[A-Z]/.test(password)) {
        score++;
    } else {
        tips.push('Add uppercase letters.');
    }
    if (/[a-z]/.test(password)) {
        score++;
    } else {
        tips.push('Add lowercase letters.');
    }
    if (/[0-9]/.test(password)) {
        score++;
    } else {
        tips.push('Add numbers.');
    }
    if (/[^A-Za-z0-9]/.test(password)) {
        score++;
    } else {
        tips.push('Add special characters (e.g. !@#$%).');
    }

    let strength = '';
    if (score === 5) {
        strength = 'Strong';
    } else if (score >= 3) {
        strength = 'Medium';
    } else {
        strength = 'Weak';
    }

    return { strength, tips };
}

// Password Generator Logic
const generateBtn = document.getElementById('generateBtn');
if (generateBtn) {
    generateBtn.addEventListener('click', function() {
        const length = parseInt(document.getElementById('gen-length').value) || 12;
        const useUpper = document.getElementById('gen-upper').checked;
        const useLower = document.getElementById('gen-lower').checked;
        const useNumber = document.getElementById('gen-number').checked;
        const useSymbol = document.getElementById('gen-symbol').checked;
        const password = generatePassword(length, useUpper, useLower, useNumber, useSymbol);
        document.getElementById('generatedPassword').value = password;
    });
}

function generatePassword(length, upper, lower, number, symbol) {
    const upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowerChars = 'abcdefghijklmnopqrstuvwxyz';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    let allChars = '';
    if (upper) allChars += upperChars;
    if (lower) allChars += lowerChars;
    if (number) allChars += numberChars;
    if (symbol) allChars += symbolChars;
    if (!allChars) return '';
    let password = '';
    for (let i = 0; i < length; i++) {
        password += allChars.charAt(Math.floor(Math.random() * allChars.length));
    }
    return password;
}

// Copy to clipboard (with checkmark animation)
const copyBtn = document.getElementById('copyBtn');
if (copyBtn) {
    copyBtn.addEventListener('click', function() {
        const pwd = document.getElementById('generatedPassword').value;
        if (pwd) {
            navigator.clipboard.writeText(pwd);
            copyBtn.classList.add('copied');
            setTimeout(() => copyBtn.classList.remove('copied'), 900);
            copyBtn.textContent = 'Copied!';
            setTimeout(() => copyBtn.textContent = 'Copy', 1200);
        }
    });
}
// Show strength for generated password
const generatedPassword = document.getElementById('generatedPassword');
const generatedStrength = document.getElementById('generatedStrength');
if (generatedPassword && generatedStrength) {
    generatedPassword.addEventListener('input', function() {
        const result = checkPasswordStrength(generatedPassword.value);
        generatedStrength.textContent = result.strength ? `Strength: ${result.strength}` : '';
        updateProgressBar(result.strength);
        showMinReqs(generatedPassword.value, result.tips);
    });
}
// Trigger strength check on generation
if (generateBtn && generatedPassword) {
    generateBtn.addEventListener('click', function() {
        setTimeout(() => {
            const event = new Event('input');
            generatedPassword.dispatchEvent(event);
            addToHistory(generatedPassword.value);
        }, 50);
    });
}
// Show/hide password
const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('password');
if (togglePassword && passwordInput) {
    togglePassword.addEventListener('click', function() {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            togglePassword.textContent = '🙈';
        } else {
            passwordInput.type = 'password';
            togglePassword.textContent = '👁️';
        }
    });
}
// Password history
const passwordHistory = document.getElementById('passwordHistory');
function addToHistory(pwd) {
    if (!pwd) return;
    let history = JSON.parse(localStorage.getItem('pwdHistory') || '[]');
    if (!history.includes(pwd)) {
        history.unshift(pwd);
        if (history.length > 5) history = history.slice(0, 5);
        localStorage.setItem('pwdHistory', JSON.stringify(history));
        renderHistory();
    }
}
function renderHistory() {
    if (!passwordHistory) return;
    let history = JSON.parse(localStorage.getItem('pwdHistory') || '[]');
    passwordHistory.innerHTML = '';
    history.forEach(pwd => {
        const li = document.createElement('li');
        li.textContent = pwd;
        const btn = document.createElement('button');
        btn.textContent = 'Copy';
        btn.onclick = () => navigator.clipboard.writeText(pwd);
        li.appendChild(btn);
        passwordHistory.appendChild(li);
    });
}
renderHistory();
// Min requirements
const minReqsDiv = document.getElementById('minReqs');
function showMinReqs(pwd, tips) {
    if (!minReqsDiv) return;
    if (!pwd) {
        minReqsDiv.textContent = '';
        return;
    }
    if (tips.length === 0) {
        minReqsDiv.textContent = 'Meets all requirements!';
        minReqsDiv.style.color = '#43a047';
    } else {
        minReqsDiv.innerHTML = 'Requirements:<ul>' + tips.map(t => `<li>${t}</li>`).join('') + '</ul>';
        minReqsDiv.style.color = '#d32f2f';
    }
}
// Progress bar (add shake for weak)
const progressBar = document.getElementById('progressBar');
function updateProgressBar(strength) {
    if (!progressBar) return;
    let width = 0, color = '#d32f2f';
    if (strength === 'Weak') { width = 33; color = '#d32f2f'; progressBar.classList.add('shake'); }
    else if (strength === 'Medium') { width = 66; color = '#fbc02d'; progressBar.classList.remove('shake'); }
    else if (strength === 'Strong') { width = 100; color = '#43a047'; progressBar.classList.remove('shake'); }
    progressBar.style.width = width + '%';
    progressBar.style.background = color;
    if (strength !== 'Weak') progressBar.classList.remove('shake');
    setTimeout(() => progressBar.classList.remove('shake'), 350);
}
// Info tooltip (already styled in CSS)
// RTL/Hebrew support
document.addEventListener('DOMContentLoaded', function() {
    const lang = navigator.language || navigator.userLanguage;
    if (lang.startsWith('he')) {
        document.documentElement.setAttribute('dir', 'rtl');
        document.querySelector('.container').setAttribute('dir', 'rtl');
    }
});
// Responsive: already handled in CSS
// Have I Been Pwned API (mocked)
function checkPwned(password) {
    // In production, use k-Anonymity API: https://haveibeenpwned.com/API/v3#PwnedPasswords
    // Here, we mock the result
    return new Promise(resolve => {
        setTimeout(() => {
            if (password.toLowerCase() === 'password' || password === '12345678') {
                resolve(true);
            } else {
                resolve(false);
            }
        }, 400);
    });
}
// Example usage: checkPwned(password).then(isPwned => { ... }); 
// Clear history button
const clearHistoryBtn = document.getElementById('clearHistoryBtn');
if (clearHistoryBtn) {
    clearHistoryBtn.addEventListener('click', function() {
        localStorage.removeItem('pwdHistory');
        renderHistory();
    });
} 