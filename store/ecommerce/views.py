from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CartItemSerializer
from .models import Product, User, CartItem

class AddCart(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user_id')
            product_id = request.data.get('product_id')
            quantity = request.data.get('quantity')

            if not quantity:
                quantity = 1
            elif int(quantity) < 1:
                return Response({'message': 'Quantity must be greater than or equal to 1'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                user = User.objects.get(id=user_id)
                product = Product.objects.get(id=product_id)
            except User.DoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            cart_item, created = CartItem.objects.get_or_create(
                session_id=user.id,
                product_id=product.id,
                defaults={'quantity': quantity}
            )

            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()

            return Response({'message': 'Item add to cart successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class GetCart(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user_id = kwargs.get('user_id')

            cart_items = CartItem.objects.filter(session_id=user_id)

            if not cart_items:
                return Response({'message': 'Cart items not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CartItemSerializer(cart_items, many=True)

            return Response({
                'data': serializer.data,
                'message': 'Ok'
            }, status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteCart(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            cart_item_id = kwargs.get('cart_item_id')

            try:
                cart_item = CartItem.objects.get(id=cart_item_id)
                cart_item.delete()
            except:
                return Response({'message': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
            
            return Response({'message': 'Ok'}, status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)