<script>
	let ptl = document.querySelectorAll(".gvirilaclass img:not(.center)");
	let rot = 360 / ptl.length;
	let rdm = 3;
	let text = document.querySelector(".gvirilaclass #text");
	
	for (let i = 0; i < ptl.length; i++) {
	  ptl[i].addEventListener("click", function () {
		this.style.opacity = "0";
		this.style.pointerEvents = "none";
		let x = Math.floor(Math.random() * 2 + 1);
		text.innerHTML = x <= 1 ? "YES" : "NO" ;
	  });
	  ptl[i].style.transform = "rotate(" + i * rdm * rot + "deg)";
	}
	
	
</script>