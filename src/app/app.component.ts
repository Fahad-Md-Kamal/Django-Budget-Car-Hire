import { Component, OnInit } from '@angular/core';
import { BlogService } from './services/blog.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  blogs = []

  constructor (private blogService: BlogService) {}

  ngOnInit() {
    this.getBlogs();
  }

  getBlogs = () => {
    this.blogService.getAllBlogs().subscribe(
      data => {
        this.blogs = data;
      }, error => {
        console.log(error);
      }
    )
  }


}
