# blog/views.py
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

#New
from converter.models import ToolAttachment
from converter.tools.pdf_to_docx_converter import pdf_to_docx_converter
from django.template import TemplateDoesNotExist


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"

# class BlogDetailView(DetailView): # new
#     model = Post
#     template_name = "post_detail.html"


# 100% working for dynamic template name of tool
class BlogDetailView(View):
    template_name = "post_detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        print(f"Debug: Received slug in URL - {slug}")
        try:
            post = Post.objects.get(slug=slug)
            toolattachment = post.toolattachment

            if toolattachment:
                # Render the tool's template and add it to the context
                tool_template = f"converter/{toolattachment.function_name}.html"
                try:
                    # Render the tool's template and add it to the context
                    tool_content = render(self.request, tool_template).content.decode('utf-8')
                    context = {'post': post, 'tool_content': tool_content}
                except TemplateDoesNotExist:
                    # Handle the case where the template doesn't exist
                    context = {'post': post, 'tool_content': f"Template not found CHECK PATH: {tool_template}"}
            else:
                context = {'post': post, 'tool_content': None}

            return render(request, self.template_name, context)
        except Post.DoesNotExist:
            print("Debug: Post does not exist with the given slug.")
            return HttpResponse("Post not found", status=404)



# 100% Working for static url with post detail
# class BlogDetailView(View):
#     template_name = "post_detail.html"

#     def get(self, request, *args, **kwargs):
#         post = Post.objects.get(slug=kwargs['slug'])
#         toolattachment = post.toolattachment

#         if toolattachment:
#             tool_template = f"converter/{toolattachment.template_name}"
#             try:
#                 tool_content = render(request, tool_template).content.decode('utf-8')
#                 return render(request, self.template_name, {'post': post, 'tool_content': tool_content})
#             except TemplateDoesNotExist:
#                 return render(request, self.template_name, {'post': post, 'tool_content': f"Template not found: {tool_template}"})
#         else:
#             return render(request, self.template_name, {'post': post, 'tool_content': None})


#working
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "post_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Retrieve the selected toolattachment
#         toolattachment = self.object.toolattachment

#         if toolattachment:
#             # Make sure the template path is correct
#             tool_template = f"converter/{toolattachment.template_name}"
#             try:
#                 # Render the tool's template and add it to the context
#                 tool_content = render(self.request, tool_template).content.decode('utf-8')
#                 context['tool_content'] = tool_content
#             except TemplateDoesNotExist:
#                 # Handle the case where the template doesn't exist
#                 context['tool_content'] = f"Template not found: {tool_template}"
#         return context
