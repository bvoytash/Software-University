import {html} from '../lib.js';
import { getAlbumById } from '../data.js';


const searchTemplate = () => html`
<section id="searchPage">
    <h1>Search by Name</h1>

    <div class="search">
        <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
        <button = class="button-list">Search</button>
    </div>

    </div>
</section>`;

const resultSearch = () => html`
<div class="search-result">
<!--If have matches-->
<div class="card-box">
    <img src="./images/BrandiCarlile.png">
    <div>
        <div class="text-center">
            <p class="name">Name: ${album.name}</p>
            <p class="artist">Artist: ${album.artist}</p>
            <p class="genre">Genre: ${album.genre}</p>
            <p class="price">Price: ${album.price}</p>
            <p class="date">Release Date: ${album.releaseDate}</p>
        </div>
        <div class="btn-group">
            <a href="/details/${album._id}" id="details">Details</a>
        </div>
    </div>
</div>`;

export async function searchPage(ctx){
    const album = await getAlbumById();
    ctx.render(searchTemplate())
}