// DOM elements
const galleryContainer = document.getElementById('galleryContainer');
const galleryGrid = document.getElementById('galleryGrid');
const imageModal = document.getElementById('imageModal');
const modalImage = document.getElementById('modalImage');
const modalImageBack = document.getElementById('modalImageBack');
const modalTitle = document.getElementById('modalTitle');
const modalDescription = document.getElementById('modalDescription');
const modalType = document.getElementById('modalType');
const modalTextBox = document.getElementById('modalTextBox');
const modalArtist = document.getElementById('modalArtist');
const modalColor = document.getElementById('modalColor');
const modalRegion = document.getElementById('modalRegion');
const descriptionRow = document.getElementById('descriptionRow');
const sortSelect = document.getElementById('sortSelect');
const modalFlipBtn = document.getElementById('modalFlipBtn');
const modalTokens = document.getElementById('modalTokens');
const tokensSection = document.getElementById('tokensSection');
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearch');
const themeToggle = document.getElementById('themeToggle');

// Store original gallery items for sorting and searching
let originalGalleryItems = [];
let filteredItems = [];
let currentSearchTerm = '';
let currentModalIndex = -1;
let currentGalleryItems = [];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    initializeEventListeners();
    setupGalleryEventListeners();
    initializeSorting();
    initializeSearch();
    handleAnimationCompletion();
});

// Initialize all event listeners
function initializeEventListeners() {
    // Modal events
    imageModal.addEventListener('click', function(e) {
        if (e.target === imageModal) {
            closeModal();
        }
    });
    
    // Keyboard events
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeModal();
        }
    });
}

// Setup gallery event listeners using event delegation
function setupGalleryEventListeners() {
    if (galleryContainer) {
        // Remove any existing listeners to prevent duplicates
        galleryContainer.removeEventListener('click', handleGalleryClick);
        // Add event listener to container for delegation
        galleryContainer.addEventListener('click', handleGalleryClick);
    }
}

// Handle gallery click events
function handleGalleryClick(e) {
    // Check if clicked on flip button
    if (e.target.closest('.flip-btn')) {
        e.stopPropagation();
        const flipBtn = e.target.closest('.flip-btn');
        const galleryItem = flipBtn.closest('.gallery-item');
        const flipContainer = galleryItem.querySelector('.card-flip-container');
        flipContainer.classList.toggle('flipped');
        return;
    }
    
    // Check if clicked on image or image container
    const galleryItem = e.target.closest('.gallery-item');
    
    if (galleryItem) {
        // Get image data directly from gallery item attributes
        const img = galleryItem.querySelector('img');
        const filename = galleryItem.getAttribute('data-filename');
        const tokens = window.tokenData && window.tokenData[filename] ? window.tokenData[filename] : [];
        
        const imageData = {
            imageUrl: img ? img.src : '',
            title: galleryItem.getAttribute('data-title') || '',
            description: galleryItem.getAttribute('data-description') || '',
            type: galleryItem.getAttribute('data-type') || '',
            textBox: galleryItem.getAttribute('data-text-box') || '',
            artist: galleryItem.getAttribute('data-artist') || '',
            color: galleryItem.getAttribute('data-color') || '',
            region: galleryItem.getAttribute('data-region') || '',
            flippable: galleryItem.getAttribute('data-flippable') === 'true',
            backUrl: galleryItem.getAttribute('data-back-url') || '',
            tokens: tokens
        };
        
        // Find the index of this item in the current gallery
        const allGalleryItems = document.querySelectorAll('.gallery-item');
        currentGalleryItems = Array.from(allGalleryItems);
        currentModalIndex = currentGalleryItems.indexOf(galleryItem);
        
        viewImage(imageData);
    }
}

// View image in modal
function viewImage(imageData) {
    modalImage.src = imageData.imageUrl;
    modalTitle.textContent = imageData.title || '';
    modalType.textContent = imageData.type || '';
    modalArtist.textContent = imageData.artist || '';
    if (modalColor) {
        modalColor.textContent = imageData.color || '';
    }
    modalRegion.textContent = imageData.region || '';
    // Convert newlines to HTML breaks for proper display
    const textBoxContent = imageData.textBox || '';
    modalTextBox.innerHTML = textBoxContent.replace(/\\n/g, '<br>').replace(/\n/g, '<br>');
    
    // Handle flippable cards in modal
    if (imageData.flippable && imageData.backUrl) {
        modalImageBack.src = imageData.backUrl;
        modalFlipBtn.style.display = 'block';
        
        // Remove any existing event listeners
        modalFlipBtn.removeEventListener('click', handleModalFlip);
        // Add flip functionality
        modalFlipBtn.addEventListener('click', handleModalFlip);
    } else {
        modalFlipBtn.style.display = 'none';
    }
    
    // Reset modal flip state
    const modalFlipContainer = document.querySelector('.modal-card-flip-container');
    if (modalFlipContainer) {
        modalFlipContainer.classList.remove('flipped');
    }
    
    // Handle tokens display
    displayTokens(imageData.tokens);
    
    // Only show description row if there's a description and the element exists
    if (descriptionRow && modalDescription && imageData.description && imageData.description.trim()) {
        modalDescription.textContent = imageData.description;
        descriptionRow.style.display = 'flex';
    } else if (descriptionRow) {
        descriptionRow.style.display = 'none';
    }
    
    imageModal.style.display = 'block';
    document.body.style.overflow = 'hidden';
    
    // Update arrow visibility based on current position
    updateArrowVisibility();
}

// Display tokens in the modal
function displayTokens(tokens) {
    if (!modalTokens || !tokensSection) return;
    
    // Clear existing tokens
    modalTokens.innerHTML = '';
    
    if (!tokens || tokens.length === 0) {
        tokensSection.style.display = 'none';
        return;
    }
    
    // Show tokens section
    tokensSection.style.display = 'block';
    
    // Create token layouts (matching main card layout)
    tokens.forEach((token, index) => {
        const tokenLayout = document.createElement('div');
        tokenLayout.className = 'token-layout';
        
        // Token image container (matching modal-image-container)
        const tokenImageContainer = document.createElement('div');
        tokenImageContainer.className = 'token-image-container';
        
        const tokenImg = document.createElement('img');
        tokenImg.src = token.url;
        tokenImg.alt = token.title || `Token ${index + 1}`;
        tokenImg.className = 'token-image';
        
        tokenImageContainer.appendChild(tokenImg);
        
        // Token info container (matching modal-info)
        const tokenInfo = document.createElement('div');
        tokenInfo.className = 'token-info';
        
        // Token title (matching modal title)
        if (token.title) {
            const tokenTitle = document.createElement('h3');
            tokenTitle.className = 'token-title';
            tokenTitle.textContent = token.title;
            tokenInfo.appendChild(tokenTitle);
        }
        
        // Token details container (matching modal-details)
        const tokenDetails = document.createElement('div');
        tokenDetails.className = 'token-details';
        
        // Token type
        if (token.type) {
            const typeRow = document.createElement('div');
            typeRow.className = 'detail-row';
            
            const typeLabel = document.createElement('span');
            typeLabel.className = 'detail-label';
            typeLabel.textContent = 'Type:';
            
            const typeValue = document.createElement('span');
            typeValue.textContent = token.type;
            
            typeRow.appendChild(typeLabel);
            typeRow.appendChild(typeValue);
            tokenDetails.appendChild(typeRow);
        }
        
        // Token text box
        if (token.text_box) {
            const textBoxRow = document.createElement('div');
            textBoxRow.className = 'detail-row text-box-row';
            
            const textBoxLabel = document.createElement('span');
            textBoxLabel.className = 'detail-label';
            textBoxLabel.textContent = 'Text Box:';
            
            const textBoxValue = document.createElement('div');
            textBoxValue.innerHTML = token.text_box.replace(/\n/g, '<br>');
            
            textBoxRow.appendChild(textBoxLabel);
            textBoxRow.appendChild(textBoxValue);
            tokenDetails.appendChild(textBoxRow);
        }
        
        tokenInfo.appendChild(tokenDetails);
        
        // Assemble token layout
        tokenLayout.appendChild(tokenImageContainer);
        tokenLayout.appendChild(tokenInfo);
        modalTokens.appendChild(tokenLayout);
    });
}

// Enlarge token in a separate modal-like overlay
function enlargeToken(tokenUrl, tokenName) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'token-overlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        z-index: 2000;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    `;
    
    // Create enlarged token image
    const enlargedImg = document.createElement('img');
    enlargedImg.src = tokenUrl;
    enlargedImg.alt = tokenName;
    enlargedImg.style.cssText = `
        max-width: 90%;
        max-height: 90%;
        border-radius: 10px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    `;
    
    // Add close functionality
    overlay.addEventListener('click', function() {
        document.body.removeChild(overlay);
    });
    
    overlay.appendChild(enlargedImg);
    document.body.appendChild(overlay);
}

// Handle modal flip button click
function handleModalFlip() {
    const modalFlipContainer = document.querySelector('.modal-card-flip-container');
    if (modalFlipContainer) {
        modalFlipContainer.classList.toggle('flipped');
    }
}

// Close modal
function closeModal() {
    imageModal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Handle animation completion to enable smooth hover transitions
function handleAnimationCompletion() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach((item, index) => {
        // Calculate when animation should complete based on delay
        const delay = (index % 5 + 1) * 100; // 0.1s, 0.2s, 0.3s, 0.4s, 0.5s
        const animationDuration = 500; // 0.5s
        const totalTime = delay + animationDuration;
        
        setTimeout(() => {
            item.classList.add('animation-complete');
        }, totalTime);
    });
}

// Initialize sorting functionality
function initializeSorting() {
    if (galleryGrid) {
        // Store original gallery items
        originalGalleryItems = Array.from(galleryGrid.children);
        
        // Add event listener to sort select
        if (sortSelect) {
            sortSelect.addEventListener('change', handleSortChange);
        }
    }
}

// Handle sort selection change
function handleSortChange() {
    const sortType = sortSelect.value;
    sortGallery(sortType);
}

// Main sorting function
function sortGallery(sortType) {
    if (!galleryContainer) return;
    
    switch (sortType) {
        case 'alphabetical':
            sortAlphabetically();
            break;
        case 'color':
            sortByColor();
            break;
        case 'region':
            sortByRegion();
            break;
        default:
            sortAlphabetically();
    }
}

// Sort alphabetically (default)
function sortAlphabetically() {
    // Clear container and restore grid layout
    galleryContainer.innerHTML = '<div class="gallery-grid" id="galleryGrid"></div>';
    const newGalleryGrid = document.getElementById('galleryGrid');
    
    // Sort items alphabetically by title
    const sortedItems = [...originalGalleryItems].sort((a, b) => {
        const titleA = a.getAttribute('data-title').toLowerCase();
        const titleB = b.getAttribute('data-title').toLowerCase();
        return titleA.localeCompare(titleB);
    });
    
    // Add sorted items to grid
    sortedItems.forEach(item => {
        newGalleryGrid.appendChild(item.cloneNode(true));
    });
    
    // Re-setup event listeners for the new grid
    setupGalleryEventListeners();
    handleAnimationCompletion();
}

// Sort by color with sections
function sortByColor() {
    // Clear container
    galleryContainer.innerHTML = '';
    
    // Define color order as specified
    const colorOrder = ['White', 'Blue', 'Black', 'Red', 'Green', 'Two Color', 'Three Color', 'Four Color','Colorless'];
    
    // Group items by color category
    const colorGroups = {};
    
    originalGalleryItems.forEach(item => {
        const colors = item.getAttribute('data-color').split(',').map(c => c.trim()).filter(c => c);
        let category;
        
        if (colors.length === 0) {
            category = 'Colorless';
        } else if (colors.length === 2) {
            category = 'Two Color';
        } else if (colors.length === 3) {
            category = 'Three Color';
        } else if (colors.length === 4) {
            category = 'Four Color';
        } else {
            category = colors[0];
        }
        
        if (!colorGroups[category]) {
            colorGroups[category] = [];
        }
        colorGroups[category].push(item);
    });
    
    // Create sections for each color in the specified order
    colorOrder.forEach(color => {
        if (colorGroups[color] && colorGroups[color].length > 0) {
            // Create section header
            const sectionHeader = document.createElement('h3');
            sectionHeader.className = 'section-header';
            sectionHeader.textContent = color;
            galleryContainer.appendChild(sectionHeader);
            
            // Create grid for this section
            const sectionGrid = document.createElement('div');
            sectionGrid.className = 'gallery-grid';
            
            // Sort items within section alphabetically
            const sortedItems = colorGroups[color].sort((a, b) => {
                const titleA = a.getAttribute('data-title').toLowerCase();
                const titleB = b.getAttribute('data-title').toLowerCase();
                return titleA.localeCompare(titleB);
            });
            
            // Add items to section grid
            sortedItems.forEach(item => {
                sectionGrid.appendChild(item.cloneNode(true));
            });
            
            galleryContainer.appendChild(sectionGrid);
        }
    });
    
    // Re-setup event listeners
    setupGalleryEventListeners();
    handleAnimationCompletion();
}

// Initialize search functionality
function initializeSearch() {
    if (searchInput && clearSearchBtn) {
        // Add search input event listener
        searchInput.addEventListener('input', handleSearchInput);
        
        // Add clear button event listener
        clearSearchBtn.addEventListener('click', clearSearch);
        
        // Add keyboard event for Enter key
        searchInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                performSearch();
            }
        });
    }
}

// Handle search input changes
function handleSearchInput(e) {
    const searchTerm = e.target.value.trim();
    currentSearchTerm = searchTerm;
    
    // Show/hide clear button
    if (searchTerm) {
        clearSearchBtn.style.display = 'flex';
    } else {
        clearSearchBtn.style.display = 'none';
    }
    
    // Perform search with debouncing
    clearTimeout(window.searchTimeout);
    window.searchTimeout = setTimeout(() => {
        performSearch();
    }, 300);
}

// Perform the actual search
function performSearch() {
    if (!currentSearchTerm) {
        // If no search term, show all items
        filteredItems = [...originalGalleryItems];
    } else {
        // Filter items based on search term
        filteredItems = originalGalleryItems.filter(item => {
            const searchLower = currentSearchTerm.toLowerCase();
            
            // Search in title
            const title = (item.getAttribute('data-title') || '').toLowerCase();
            if (title.includes(searchLower)) return true;
            
            // Search in type
            const type = (item.getAttribute('data-type') || '').toLowerCase();
            if (type.includes(searchLower)) return true;
            
            // Search in regions
            const regions = (item.getAttribute('data-region') || '').toLowerCase();
            if (regions.includes(searchLower)) return true;
            
            // Search in text box
            const textBox = (item.getAttribute('data-text-box') || '').toLowerCase();
            if (textBox.includes(searchLower)) return true;
            
            // Search in artist
            const artist = (item.getAttribute('data-artist') || '').toLowerCase();
            if (artist.includes(searchLower)) return true;
            
            // Search in colors
            const colors = (item.getAttribute('data-color') || '').toLowerCase();
            if (colors.includes(searchLower)) return true;
            
            return false;
        });
    }
    
    // Update the gallery display
    displayFilteredItems();
}

// Display filtered items
function displayFilteredItems() {
    if (!galleryContainer) return;
    
    // Clear container and create new grid
    galleryContainer.innerHTML = '<div class="gallery-grid" id="galleryGrid"></div>';
    const newGalleryGrid = document.getElementById('galleryGrid');
    
    if (filteredItems.length === 0) {
        // Show no results message
        galleryContainer.innerHTML = `
            <div class="empty-gallery">
                <i class="fas fa-search empty-icon"></i>
                <h3>No cards found</h3>
                <p>No cards match your search criteria. Try different keywords.</p>
            </div>
        `;
    } else {
        // Sort filtered items alphabetically by default
        const sortedItems = [...filteredItems].sort((a, b) => {
            const titleA = a.getAttribute('data-title').toLowerCase();
            const titleB = b.getAttribute('data-title').toLowerCase();
            return titleA.localeCompare(titleB);
        });
        
        // Add filtered items to grid
        sortedItems.forEach(item => {
            newGalleryGrid.appendChild(item.cloneNode(true));
        });
    }
    
    // Re-setup event listeners for the new grid
    setupGalleryEventListeners();
    handleAnimationCompletion();
}

// Clear search
function clearSearch() {
    searchInput.value = '';
    currentSearchTerm = '';
    clearSearchBtn.style.display = 'none';
    
    // Reset to show all items
    filteredItems = [...originalGalleryItems];
    displayFilteredItems();
    
    // Focus back on search input
    searchInput.focus();
}

// Update sorting functions to work with filtered items
function sortAlphabetically() {
    // Use filtered items if search is active, otherwise use all items
    const itemsToSort = currentSearchTerm ? filteredItems : originalGalleryItems;
    
    // Clear container and restore grid layout
    galleryContainer.innerHTML = '<div class="gallery-grid" id="galleryGrid"></div>';
    const newGalleryGrid = document.getElementById('galleryGrid');
    
    // Sort items alphabetically by title
    const sortedItems = [...itemsToSort].sort((a, b) => {
        const titleA = a.getAttribute('data-title').toLowerCase();
        const titleB = b.getAttribute('data-title').toLowerCase();
        return titleA.localeCompare(titleB);
    });
    
    // Add sorted items to grid
    sortedItems.forEach(item => {
        newGalleryGrid.appendChild(item.cloneNode(true));
    });
    
    // Re-setup event listeners for the new grid
    setupGalleryEventListeners();
    handleAnimationCompletion();
}

// Update color sorting to work with filtered items
function sortByColor() {
    // Use filtered items if search is active, otherwise use all items
    const itemsToSort = currentSearchTerm ? filteredItems : originalGalleryItems;
    
    // Clear container
    galleryContainer.innerHTML = '';
    
    // Define color order as specified
    const colorOrder = ['White', 'Blue', 'Black', 'Red', 'Green', 'Two Color', 'Three Color', 'Four Color','Colorless'];
    
    // Group items by color category
    const colorGroups = {};
    
    itemsToSort.forEach(item => {
        const colors = item.getAttribute('data-color').split(',').map(c => c.trim()).filter(c => c);
        let category;
        
        if (colors.length === 0) {
            category = 'Colorless';
        } else if (colors.length === 2) {
            category = 'Two Color';
        } else if (colors.length === 3) {
            category = 'Three Color';
        } else if (colors.length === 4) {
            category = 'Four Color';
        } else {
            category = colors[0];
        }
        
        if (!colorGroups[category]) {
            colorGroups[category] = [];
        }
        colorGroups[category].push(item);
    });
    
    // Create sections for each color in the specified order
    colorOrder.forEach(color => {
        if (colorGroups[color] && colorGroups[color].length > 0) {
            // Create section header
            const sectionHeader = document.createElement('h3');
            sectionHeader.className = 'section-header';
            sectionHeader.textContent = color;
            galleryContainer.appendChild(sectionHeader);
            
            // Create grid for this section
            const sectionGrid = document.createElement('div');
            sectionGrid.className = 'gallery-grid';
            
            // Sort items within section alphabetically
            const sortedItems = colorGroups[color].sort((a, b) => {
                const titleA = a.getAttribute('data-title').toLowerCase();
                const titleB = b.getAttribute('data-title').toLowerCase();
                return titleA.localeCompare(titleB);
            });
            
            // Add items to section grid
            sortedItems.forEach(item => {
                sectionGrid.appendChild(item.cloneNode(true));
            });
            
            galleryContainer.appendChild(sectionGrid);
        }
    });
    
    // Re-setup event listeners
    setupGalleryEventListeners();
    handleAnimationCompletion();
}

// Update region sorting to work with filtered items
function sortByRegion() {
    // Use filtered items if search is active, otherwise use all items
    const itemsToSort = currentSearchTerm ? filteredItems : originalGalleryItems;
    
    // Clear container
    galleryContainer.innerHTML = '';
    
    // Group items by region
    const regionGroups = {};
    
    itemsToSort.forEach(item => {
        const regions = item.getAttribute('data-region').split(',').map(r => r.trim()).filter(r => r);
        
        if (regions.length === 0) {
            if (!regionGroups['Unknown']) {
                regionGroups['Unknown'] = [];
            }
            regionGroups['Unknown'].push(item);
        } else {
            // Add item to each region it belongs to
            regions.forEach(region => {
                if (!regionGroups[region]) {
                    regionGroups[region] = [];
                }
                regionGroups[region].push(item);
            });
        }
    });
    
    // Sort regions alphabetically
    const sortedRegions = Object.keys(regionGroups).sort();
    
    // Create sections for each region
    sortedRegions.forEach(region => {
        if (regionGroups[region] && regionGroups[region].length > 0) {
            // Create section header
            const sectionHeader = document.createElement('h3');
            sectionHeader.className = 'section-header';
            sectionHeader.textContent = region;
            galleryContainer.appendChild(sectionHeader);
            
            // Create grid for this section
            const sectionGrid = document.createElement('div');
            sectionGrid.className = 'gallery-grid';
            
            // Sort items within section alphabetically
            const sortedItems = regionGroups[region].sort((a, b) => {
                const titleA = a.getAttribute('data-title').toLowerCase();
                const titleB = b.getAttribute('data-title').toLowerCase();
                return titleA.localeCompare(titleB);
            });
            
            // Add items to section grid
            sortedItems.forEach(item => {
                sectionGrid.appendChild(item.cloneNode(true));
            });
            
            galleryContainer.appendChild(sectionGrid);
        }
    });
    
    // Re-setup event listeners
    setupGalleryEventListeners();
    handleAnimationCompletion();
}

// Modal navigation functions

function navigateModal(direction) {
    if (currentModalIndex === -1 || currentGalleryItems.length === 0) return;
    
    let newIndex;
    if (direction === 'prev') {
        newIndex = currentModalIndex - 1;
        if (newIndex < 0) {
            return; // Don't wrap around, just return
        }
    } else if (direction === 'next') {
        newIndex = currentModalIndex + 1;
        if (newIndex >= currentGalleryItems.length) {
            return; // Don't wrap around, just return
        }
    }
    
    // Update current index
    currentModalIndex = newIndex;
    
    // Get the new gallery item
    const newGalleryItem = currentGalleryItems[newIndex];
    
    // Extract image data from the gallery item
    const img = newGalleryItem.querySelector('img');
    const filename = newGalleryItem.getAttribute('data-filename');
    const tokens = window.tokenData && window.tokenData[filename] ? window.tokenData[filename] : [];
    
    const imageData = {
        imageUrl: img ? img.src : '',
        title: newGalleryItem.getAttribute('data-title') || '',
        description: newGalleryItem.getAttribute('data-description') || '',
        type: newGalleryItem.getAttribute('data-type') || '',
        textBox: newGalleryItem.getAttribute('data-text-box') || '',
        artist: newGalleryItem.getAttribute('data-artist') || '',
        color: newGalleryItem.getAttribute('data-color') || '',
        region: newGalleryItem.getAttribute('data-region') || '',
        flippable: newGalleryItem.getAttribute('data-flippable') === 'true',
        backUrl: newGalleryItem.getAttribute('data-back-url') || '',
        tokens: tokens
    };
    
    // Update the modal with new data
    viewImage(imageData);
    
    // Update arrow visibility
    updateArrowVisibility();
}

// Update arrow visibility based on current position
function updateArrowVisibility() {
    const prevArrow = document.querySelector('.modal-nav-prev');
    const nextArrow = document.querySelector('.modal-nav-next');
    
    if (prevArrow && nextArrow) {
        // Hide left arrow if at first card
        prevArrow.style.display = currentModalIndex === 0 ? 'none' : 'flex';
        
        // Hide right arrow if at last card
        nextArrow.style.display = currentModalIndex === currentGalleryItems.length - 1 ? 'none' : 'flex';
    }
}

// Add keyboard navigation for modal
function initializeModalKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        // Only handle keyboard navigation when modal is open
        if (imageModal.style.display === 'block') {
            if (e.key === 'ArrowLeft') {
                e.preventDefault();
                navigateModal('prev');
            } else if (e.key === 'ArrowRight') {
                e.preventDefault();
                navigateModal('next');
            }
        }
    });
}

// Initialize modal keyboard navigation
initializeModalKeyboardNavigation();

// Theme functionality
function initializeTheme() {
    // Check for saved theme preference or default to 'light'
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    
    // Add event listener to theme toggle button
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
}

function toggleTheme() {
    const currentTheme = document.body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    // Update the theme
    document.body.setAttribute('data-theme', newTheme);
    
    // Save theme preference
    localStorage.setItem('theme', newTheme);
    
    // Add a subtle animation effect
    document.body.style.transition = 'all 0.3s ease';
    setTimeout(() => {
        document.body.style.transition = '';
    }, 300);
}
