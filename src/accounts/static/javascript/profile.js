// Client-side image preview for profile upload
document.addEventListener('DOMContentLoaded', function(){
  let fileInput = document.querySelector('input[type=file][name="profile_pic"]');
  const imgPreview = document.querySelector('.profile-avatar');
  if (!fileInput) {
    // try to find by label's for attribute
    const label = document.querySelector('label[for]');
    if (label) {
      const id = label.getAttribute('for');
      fileInput = document.getElementById(id);
    }
  }
  if (!fileInput) return;

  fileInput.addEventListener('change', function(e){
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(ev){
      if (imgPreview) imgPreview.src = ev.target.result;
    };
    reader.readAsDataURL(file);
  });
});
