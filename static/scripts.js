document.addEventListener('DOMContentLoaded', () => {
    const categoryButtons = document.querySelectorAll('.category-btn');
    const ideaDisplay = document.querySelector('#idea-display');
    const ideaText = document.querySelector('.idea-text');
    const loadingSpinner = document.querySelector('.loading-spinner');
    const saveButton = document.getElementById('save-idea');
    const shareButton = document.getElementById('share-idea');
    const toggleSavedButton = document.getElementById('toggle-saved');
    const savedIdeasPanel = document.querySelector('.saved-ideas');
    const notification = document.getElementById('notification');
    let currentIdea = '';

    const showNotification = (message) => {
        notification.textContent = message;
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    };

    const generateIdea = async (category) => {
        ideaText.classList.remove('visible');
        loadingSpinner.style.display = 'block';
        
        try {
            const response = await fetch(`/generate/${category}`);
            const data = await response.json();
            
            if (data.error) throw new Error(data.error);
            
            currentIdea = data.idea;
            ideaText.textContent = currentIdea;
            
            setTimeout(() => {
                loadingSpinner.style.display = 'none';
                ideaText.classList.add('visible');
            }, 500);
        } catch (error) {
            ideaText.textContent = 'Oops! Something went wrong. Please try again.';
            loadingSpinner.style.display = 'none';
            ideaText.classList.add('visible');
        }
    };

    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            generateIdea(button.dataset.category);
        });
    });

    saveButton.addEventListener('click', () => {
        if (!currentIdea) return;
        
        let savedIdeas = JSON.parse(localStorage.getItem('savedIdeas') || '[]');
        if (!savedIdeas.includes(currentIdea)) {
            savedIdeas.push(currentIdea);
            localStorage.setItem('savedIdeas', JSON.stringify(savedIdeas));
            updateSavedIdeasList();
            showNotification('Idea saved successfully!');
        } else {
            showNotification('This idea is already saved!');
        }
    });

    shareButton.addEventListener('click', () => {
        if (!currentIdea) return;
        
        const shareData = {
            title: 'Check out this idea from Ideator!',
            text: currentIdea,
            url: window.location.href
        };

        if (navigator.share) {
            navigator.share(shareData)
                .catch(() => {
                    // Fallback to clipboard copy
                    navigator.clipboard.writeText(currentIdea);
                    showNotification('Idea copied to clipboard!');
                });
        } else {
            navigator.clipboard.writeText(currentIdea);
            showNotification('Idea copied to clipboard!');
        }
    });

    toggleSavedButton.addEventListener('click', () => {
        savedIdeasPanel.classList.toggle('open');
    });

    const updateSavedIdeasList = () => {
        const savedIdeasList = document.getElementById('saved-ideas-list');
        const savedIdeas = JSON.parse(localStorage.getItem('savedIdeas') || '[]');
        
        savedIdeasList.innerHTML = savedIdeas.map(idea => `
            <div class="saved-idea-item">
                <p>${idea}</p>
                <button class="btn btn-sm btn-outline-light mt-2" onclick="navigator.clipboard.writeText('${idea}')">
                    <i class="fas fa-copy"></i>
                </button>
            </div>
        `).join('');
    };

    // Initialize saved ideas list
    updateSavedIdeasList();
});
