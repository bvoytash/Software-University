import {html} from '../lib.js';
import { getUserData } from '../api/util.js';
import { deleteItem, getById } from '../data.js';

const detailsTemplate = (album, isOwner, onDelete) => html`
<section id="detailsPage">
    <div class="wrapper">
        <div class="albumCover">
            <img src="${album.imgUrl}">
        </div>
        <div class="albumInfo">
            <div class="albumText">

                <h1>Name: ${album.name}</h1>
                <h3>Artist: ${album.artist}</h3>
                <h4>Genre: ${album.genre}</h4>
                <h4>Price: ${album.price}</h4>
                <h4>Date: ${album.releaseDate}</h4>
                <p>D${album.description}</p>
            </div>

            <!-- Only for registered user and creator of the album-->
            <div class="actionBtn">
                ${isOwner ? html`
                <a href="/edit/${album._id}" class="edit">Edit</a>
                <a href="#" class="remove" @click="${onDelete}" >Delete</a>` : null}
            </div>
        </div>
    </div>
</section>`;


export async function detailsAlbum(ctx){
    const userData = getUserData();
    const album = await getById(ctx.params.id);

    const isOwner = userData && userData.id == album._ownerId;
    ctx.render(detailsTemplate(album, isOwner, onDelete));

    async function onDelete(){
        const choice = confirm('Are you sure?');
        if(choice){
            await deleteItem(ctx.params.id);
            ctx.page.redirect('/');
        }
    }
}
