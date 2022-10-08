from dependency_injector import containers, providers
from client.infrastructure.logging.client_logger import ClientLogger
from client.infrastructure.logging.logger_config_factory import create_logger_config
from client.infrastructure.settings.settings import Settings
from client.repositories.order_repository import OrderRepository
from client.services.order_service import OrderService
from client.services.payment_service_stub import PaymentServiceStub
from structured_logging.logger.logger import Logger
from structured_logging.logger_creation.logger_factory import create_logger


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    # NOTE: we are recreating the settings object here because dependency injection in python is bit dense in passing the configuration
    external_logger: Logger = providers.Object(
        create_logger(create_logger_config(Settings())))
    
    __logger_provider = providers.Singleton(ClientLogger, 
                                    external_logger= external_logger)

    __payment_provider = providers.Singleton(PaymentServiceStub,
                                    should_succeed=config.should_payment_succeed,
                                    logger=__logger_provider)

    __order_repository_provider = providers.Singleton(OrderRepository, 
                                    file_name=config.order_file_path)

    order_service = providers.Singleton(OrderService,
                                    payment_service=__payment_provider,
                                    order_repository=__order_repository_provider,
                                    logger=__logger_provider)
    


    

