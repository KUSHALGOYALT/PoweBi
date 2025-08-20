// Simple Authentication System JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Basic form submission enhancement
    const loginForm = document.querySelector('form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const submitBtn = loginForm.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.textContent = 'Signing In...';
                submitBtn.disabled = true;
                
                // Re-enable after 3 seconds (in case of error)
                setTimeout(() => {
                    submitBtn.textContent = 'Sign In';
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    }
});