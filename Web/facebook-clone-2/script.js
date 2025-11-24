const followBtn = document.querySelector('#follow-btn');

// Boolean: True / False
let isFollowing = false;

followBtn.addEventListener('click', () => {
    // alert('Hello!!')

    followBtn.innerHTML = '<div class="loader"></div>';
    
    setTimeout(() => {
        
        // followBtn.innerHTML = '';
        
        if (isFollowing) {
            followBtn.textContent = 'Follow';
            followBtn.style.backgroundColor = '#006aed';
        } else {
            followBtn.textContent = 'Following';
            followBtn.style.backgroundColor = '#9e7396b2';
        }

        isFollowing = !isFollowing;
    }, 2000);

});

