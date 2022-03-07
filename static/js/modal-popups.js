function closeModal() {
    const container = document.getElementById("modals-here");
    const backdrop = document.getElementById("modal-backdrop");
    const modal = document.getElementById("modal");

    modal.classList.remove("show")
	backdrop.classList.remove("show")

	setTimeout(function () {
            container.removeChild(backdrop);
            container.removeChild(modal);
        },
        200)
}
